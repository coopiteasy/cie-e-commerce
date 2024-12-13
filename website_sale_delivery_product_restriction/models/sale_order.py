# Copyright 2022 Coop IT Easy SC
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _get_delivery_methods(self):
        products = list(self.order_line.mapped("product_id"))
        return (
            super()
            ._get_delivery_methods()
            .filtered(lambda c: c._can_be_used_to_deliver_products(products))
        )
