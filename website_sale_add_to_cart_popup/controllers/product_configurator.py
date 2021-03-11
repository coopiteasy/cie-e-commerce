# Copyright 2021 Coop IT Easy SCRLfs <https://coopiteasy.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields
from odoo.http import request

from odoo.addons.sale.controllers.product_configurator import (
    ProductConfiguratorController,
)


class ProductConfiguratorController(ProductConfiguratorController):
    def _show_optional_products(
        self, product_id, variant_values, pricelist, handle_stock, **kw
    ):
        """
        Overwrite default behaviour to always show a content for the
        add to cart modal.
        """
        product = (
            request.env["product.product"]
            .with_context(self._get_product_context(pricelist, **kw))
            .browse(int(product_id))
        )
        combination = request.env["product.template.attribute.value"].browse(
            variant_values
        )

        add_qty = int(kw.get("add_qty", 1))
        to_currency = (pricelist or product).currency_id
        company = (
            request.env["res.company"].browse(
                request.env.context.get("company_id")
            )
            or request.env["res.users"]._get_company()
        )
        date = request.env.context.get("date") or fields.Date.today()

        def compute_currency(price):
            return product.currency_id._convert(
                price, to_currency, company, date
            )

        no_variant_attribute_values = combination.filtered(
            lambda rec: rec.attribute_id.create_variant == "no_variant"
        )
        if no_variant_attribute_values:
            product = product.with_context(
                no_variant_attribute_values=no_variant_attribute_values
            )

        return request.env["ir.ui.view"].render_template(
            "sale.optional_products_modal",
            {
                "product": product,
                "combination": combination,
                "add_qty": add_qty,
                # reference_product deprecated, use combination instead
                "reference_product": product,
                "variant_values": variant_values,
                "pricelist": pricelist,
                # compute_currency deprecated, get from pricelist or product
                "compute_currency": compute_currency,
                # to_currency deprecated, get from pricelist or product
                "to_currency": to_currency,
                "handle_stock": handle_stock,
                # get_attribute_exclusions deprecated, use product method
                "get_attribute_exclusions": self._get_attribute_exclusions,
            },
        )
