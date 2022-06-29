# Copyright 2021 Coop IT Easy SC <http://coopiteasy.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.template"

    customer_type_ids = fields.Many2many(
        string="Restricted by Customer Types",
        comodel_name="res.partner.customer.type",
        columns2="website_product_ids",
        help=(
            "This product appears in restriction list of the following "
            "customer type"
        )
    )
