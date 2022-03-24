# Copyright 2021 Coop IT Easy SCRLfs <https://coopiteasy.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.http import request

from odoo.addons.sale_product_configurator.controllers.main import (
    ProductConfiguratorController,
)


class ProductConfiguratorController(ProductConfiguratorController):
    def _show_optional_products(
        self, product_id, variant_values, pricelist, handle_stock, **kw
    ):
        """
        Overwrite default behaviour to always show a content for the
        add to cart modal.

        Copied verbatim from sale_product_configurator, and slightly adjusted.
        """
        product = request.env["product.product"].browse(int(product_id))
        combination = request.env["product.template.attribute.value"].browse(
            variant_values
        )
        # Commented out from upstream. Preserved for posterity's sake.
        #
        # has_optional_products = product.optional_product_ids.filtered(
        #     lambda p: p._is_add_to_cart_possible(combination)
        # )
        #
        # if not has_optional_products:
        #     return False

        add_qty = int(kw.get("add_qty", 1))

        no_variant_attribute_values = combination.filtered(
            lambda attribute_value: attribute_value.attribute_id.create_variant
            == "no_variant"
        )
        if no_variant_attribute_values:
            product = product.with_context(
                no_variant_attribute_values=no_variant_attribute_values
            )

        return request.env["ir.ui.view"]._render_template(
            "sale_product_configurator.optional_products_modal",
            {
                "product": product,
                "combination": combination,
                "add_qty": add_qty,
                "parent_name": product.name,
                "variant_values": variant_values,
                "pricelist": pricelist,
                "handle_stock": handle_stock,
            },
        )
