# Copyright 2021 Coop IT Easy SC <http://coopiteasy.be>
#   Rémy Taymans <remy@coopiteasy.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResPartnerCustomerType(models.Model):
    _inherit = "res.partner.customer.type"

    website_restrict_acquirer = fields.Boolean(
        string="Restrict Acquirer on E-commerce"
    )
    website_acquirer_ids = fields.Many2many(
        string="Acquirers",
        comodel_name="payment.acquirer",
        columns2="customer_type_ids",
        domain=[('website_published', '=', True)],
        help="Acquirers enabled for this Customer Type"
    )
