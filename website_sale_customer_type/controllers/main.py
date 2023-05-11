# Copyright 2018 Coop IT Easy SCRLfs
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, http
from odoo.http import request

from odoo.addons.website_sale.controllers.main import (
    PPG,
    TableCompute,
    WebsiteSale as Base,
)


class WebsiteSale(Base):
    def _is_product_allowed(self, product_tmpl, allowed_products):
        """
        Return True if the product_tmpl is allowed based on the
        allowed_products list.
        product_tmpl must be a product.template.
        """
        # TODO: Validate this when product_variant is not activate !
        for variant in product_tmpl.product_variant_ids:
            if allowed_products is not None and variant in allowed_products:
                return True
            elif allowed_products is None:
                return True
        return False

    @http.route()
    def shop(self, page=0, category=None, search="", ppg=False, **post):
        """
        This function overwrite the shop function to filter the product
        that will be shown on this page. As the amount of product will
        be different than in the original function, page number should
        be recalculated.
        """
        # Set product per page
        if ppg:
            try:
                ppg = int(ppg)
            except ValueError:
                ppg = PPG
        else:
            ppg = PPG

        # Call the parent function and get all of the products
        response = super().shop(
            page=0, category=category, search=search, ppg="10000", **post
        )
        products = response.qcontext["products"]

        # Get current user list of products (product.product)
        if request.env.user.website_restrict_product:
            allowed_products = request.env.user.website_product_ids
        else:
            allowed_products = None

        # Filter products
        products = products.filtered(
            lambda p: self._is_product_allowed(p, allowed_products)
        )

        # Construct pager
        keep = response.qcontext["keep"]
        product_count = len(products.ids)
        post.update({key: val for key, val in keep.args.items() if val})
        pager = request.website.pager(
            url=keep.path,
            total=product_count,
            page=page,
            step=ppg,
            scope=7,
            url_args=post,
        )

        # Truncate product according to the pager
        products = products[pager["offset"] : pager["offset"] + ppg]

        # Add element to context
        response.qcontext["products"] = products
        response.qcontext[
            "restrict_product"
        ] = request.env.user.website_restrict_product
        response.qcontext["allowed_products"] = allowed_products
        response.qcontext["product_count"] = product_count
        response.qcontext["pager"] = pager
        response.qcontext["bins"] = TableCompute().process(products, ppg)
        return response

    @http.route()
    def product(self, product, category="", search="", **kwargs):
        response = super().product(product, category, search, **kwargs)

        # Get product list allowed for the current user (product.product)
        if request.env.user.website_restrict_product:
            allowed_products = request.env.user.website_product_ids
        else:
            allowed_products = None

        # Filter alternative_product_ids
        if allowed_products is not None:
            allowed_product_tmpls = allowed_products.mapped("product_tmpl_id")
            alt_product_ids = product.alternative_product_ids.filtered(
                lambda p: p in allowed_product_tmpls
            )
        else:
            alt_product_ids = product.alternative_product_ids
        response.qcontext["allowed_products"] = allowed_products
        response.qcontext[
            "restrict_product"
        ] = request.env.user.website_restrict_product
        response.qcontext["alt_product_ids"] = alt_product_ids
        return response

    def _get_shop_payment_values(self, order, **kwargs):
        result = super(WebsiteSale, self)._get_shop_payment_values(order, **kwargs)
        shipping_partner_id = False
        if order:
            shipping_partner_id = (
                order.partner_shipping_id.id or order.partner_invoice_id.id
            )
        allowed_acquirers = {}
        if request.env.user.website_restrict_acquirer:
            allowed_acquirers = request.env.user.website_acquirer_ids

        form_acquirers = [
            acq
            for acq in allowed_acquirers
            if acq.payment_flow == "form" and acq.view_template_id
        ]
        s2s_acquirers = [
            acq
            for acq in allowed_acquirers
            if acq.payment_flow == "s2s" and acq.registration_view_template_id
        ]

        for acq in form_acquirers:
            acq.form = (
                acq.with_context(
                    submit_class="btn btn-primary", submit_txt=_("Pay Now")
                )
                .sudo()
                .render(
                    "/",
                    order.amount_total,
                    order.pricelist_id.currency_id.id,
                    values={
                        "return_url": "/shop/payment/validate",
                        "partner_id": shipping_partner_id,
                        "billing_partner_id": order.partner_invoice_id.id,
                    },
                )
            )

        if form_acquirers:
            result["form_acquirers"] = form_acquirers
        if s2s_acquirers:
            result["s2s_acquirers"] = s2s_acquirers

        return result
