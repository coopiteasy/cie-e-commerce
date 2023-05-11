# Copyright 2020 Coop IT Easy SCRLfs <http://coopiteasy.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    customer_type_ids = fields.Many2many(
        string="Restricted by Customer Types",
        comodel_name="res.partner.customer.type",
        columns2="website_product_ids",
        help=(
            "This product appears in restriction list of the following " "customer type"
        ),
    )
