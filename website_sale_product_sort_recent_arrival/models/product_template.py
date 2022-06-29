# Copyright 2022 Coop IT Easy SC
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models


class ProductTemplate(models.Model):

    _inherit = "product.template"

    recent_arrival_date = fields.Date(
        string="Recent Arrival Date",
        default=fields.Date.today(),
        help="Date of the most recent arrival for this product.",
    )
