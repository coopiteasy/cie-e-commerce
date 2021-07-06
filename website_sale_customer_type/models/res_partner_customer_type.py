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
    next_url = fields.Char(
        string="Redirection URL",
        default="",
        help=(
            "URL used to redirect the user after selecting customer type "
            "on e-commerce."
        )
    )
    show_on_website = fields.Boolean(
        string="Show on website",
        default=True,
        help="Show on the Customer Type Selector on the e-commerce"
    )
    website_require_early_login = fields.Boolean(
        string="Require Early Login",
        default=False,
        help="User will be force to connect before accessing the e-commerce"
    )
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

    def show_on_website_button(self):
        """Toggle function used for the button in the form"""
        for rec in self:
            rec.show_on_website = not rec.show_on_website
