# Copyright 2022 Coop IT Easy SC
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    # another way would be to override
    # delivery.carrier._is_available_for_order() (defined in the delivery
    # module and called by sale.order._get_delivery_methods() in the
    # website_sale_delivery module), but this would have to map the products
    # for each delivery.carrier, so this is more optimal.
    def _get_delivery_methods(self):
        products = list(self.order_line.mapped("product_id"))
        return (
            super()
            ._get_delivery_methods()
            .filtered(lambda c: c._can_be_used_to_deliver_products(products))
        )
