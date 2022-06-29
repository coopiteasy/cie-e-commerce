# Copyright 2022 Coop IT Easy SC
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, models


class Website(models.Model):

    _inherit = "website"

    @api.model
    def _get_product_sort_criterias(self):
        res = super()._get_product_sort_criterias()
        res.append(
            (
                "recent_arrival_date desc",
                _("Recent Arrival Date (Recent first)"),
            )
        )
        return res
