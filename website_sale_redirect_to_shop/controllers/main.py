# SPDX-FileCopyrightText: 2023 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import http
from odoo.http import request

from odoo.addons.website_sale.controllers.main import WebsiteSale


class RedirectWebsiteSale(WebsiteSale):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @http.route(
        ["/shop/cart/update"],
        type="http",
        auth="public",
        methods=["POST"],
        website=True,
        csrf=False,
    )
    def cart_update(self, product_id, add_qty=1, set_qty=0, **kw):
        super().cart_update(product_id, add_qty=add_qty, set_qty=set_qty, **kw)
        return request.redirect("/shop")
