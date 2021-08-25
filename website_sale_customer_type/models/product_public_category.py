# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models, api


class ProductPublicCategory(models.Model):
    _inherit = 'product.public.category'

    is_display_stand = fields.Boolean(
        string="Is A Display Stand?"
    )
    customer_type_ids = fields.Many2many(
        string="Restricted by Customer Types",
        comodel_name="res.partner.customer.type",
        columns2="website_public_categ_ids",
        help=(
            "This product appears in restriction list of the following "
            "customer type"
        )
    )
