# Copyright 2019-Today Coop IT Easy SCRLfs
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):

    _inherit = "res.config.settings"

    is_ecommerce_open = fields.Boolean(
        string="Is e-commerce open",
        default=True,
        help="When checked, e-commerce is open. When unchecked, "
        "e-commerce is closed.",
        related="website_id.is_ecommerce_open",
        readonly=False,
    )
    text_closed_ecommerce = fields.Html(
        string="Text closed e-commerce",
        default="E-commerce is momently closed.",
        translate=True,
        related="website_id.text_closed_ecommerce",
        readonly=False,
    )
