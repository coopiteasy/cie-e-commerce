# Copyright 2021 Coop IT Easy SCRLfs <http://coopiteasy.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class StockMove(models.Model):
    _inherit = 'stock.move'

    @api.model
    def create(self, values):
        move = super(StockMove, self).create(values)
        move.product_tmpl_id.website_auto_publish()
        return move

    @api.multi
    def write(self, values):
        res = super(StockMove, self).write(values)
        self.mapped('product_tmpl_id').website_auto_publish()
        return res
