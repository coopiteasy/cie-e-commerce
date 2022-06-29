# Copyright 2021 Coop IT Easy SC <http://coopiteasy.be>
#   Rémy Taymans <remy@coopiteasy.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResPartnerCustomerType(models.Model):
    _inherit = "res.partner.customer.type"

    website_restrict_signup = fields.Boolean(
        string="Restrict Signup on E-commerce",
        help="Specify whether the customer type is allowed to create an account on e-commerce",
    )
    website_restrict_signup_text = fields.Char(
        string="Custom text for signup restriction",
        default="Signup is restricted for this customer type",
        translate=True
    )
    website_signup_vat_required = fields.Boolean(
        string="Require TIN/VAT number for signup",
        help="Specify whether the customer type must specify the TIN/VAT number on signup",
    )
    website_signup_vat_required_text = fields.Char(
        string="Custom text for VAT number requirement",
        default="A TIN/VAT number is required for this customer type",
        translate=True
    )
