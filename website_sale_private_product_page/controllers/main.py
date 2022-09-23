# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from werkzeug.exceptions import Forbidden, NotFound

from odoo import http
from odoo.http import request

from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSalePrivateToken(WebsiteSale):
    def _has_access_if_unpublished(self):
        # All users logged in with an Odoo back-end account (base.group_user)
        # can see unpublished products (greyed out) on the /shop page.
        return request.env.user.has_group("base.group_user")

    def _get_search_domain(self, search, category, attrib_values):
        # The search domain applies to all searches and product lists on /shop.
        # By default, it depends on record rules to forbid public users from
        # accessing unpublished pages. In this module, we create a record rule
        # that grants public users the right to view unpublished products that
        # have private tokens. We do not want these products to show up to all
        # users; they can only be accessed by token. However, authorised users
        # should still be able to see unpublished products.
        result = super()._get_search_domain(search, category, attrib_values)
        # Back-end users.
        if self._has_access_if_unpublished():
            return result
        # Public users.
        return result + [("website_published", "=", True)]

    @http.route(
        ["/shop/private_product/<string:token>"],
        type="http",
        auth="public",
        website=True,
    )
    def private_product(self, token, category="", search="", **kwargs):
        product = request.env["product.template"].search(
            [("private_url_token", "=", token)]
        )
        if not product:
            raise NotFound()
        return self.product(
            product,
            category=category,
            search=search,
            published_check=False,
            **kwargs,
        )

    @http.route()
    def product(self, product, category="", search="", **kwargs):
        if (
            kwargs.get("published_check", True)
            and not product.website_published
            and not self._has_access_if_unpublished()
        ):
            raise Forbidden()
        return super().product(product, category=category, search=search, **kwargs)
