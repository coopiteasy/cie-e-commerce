# Copyright 2022 Coop IT Easy SC
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class SaleOrder(models.Model):

    _inherit = "sale.order"

    def _get_delivery_methods(self):
        return self.available_carrier_ids.filtered(
            lambda c: c.website_published
        )
