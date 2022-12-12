# Copyright 2020 Coop IT Easy SCRLfs <http://coopiteasy.be>
#   Rémy Taymans <remy@coopiteasy.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResPartnerCustomerType(models.Model):
    _description = "Customer Type"
    _order = "name"
    _name = "res.partner.customer.type"

    name = fields.Char(
        string="Customer Type Name",
        required=True,
        translate=True
    )
    active = fields.Boolean(default=True)
    website_restrict_product = fields.Boolean(
        string="Restrict Product on E-commerce"
    )
    website_product_ids = fields.Many2many(
        string="Product",
        comodel_name="product.product",
        columns2="customer_type_ids",
        help=(
            "Choose product that can be viewed on e-commerce by users "
            "that belongs to this customer type."
        )
    )
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
