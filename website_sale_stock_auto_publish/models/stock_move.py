# Copyright 2021 Coop IT Easy SC <http://coopiteasy.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class StockMove(models.Model):
    _inherit = "stock.move"

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        records.product_tmpl_id.website_auto_publish()
        return records

    def write(self, values):
        res = super().write(values)
        self.product_tmpl_id.website_auto_publish()
        return res
