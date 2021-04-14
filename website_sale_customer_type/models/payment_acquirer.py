from odoo import fields, models


class PaymentAcquirer(models.Model):
    _inherit = "payment.acquirer"

    customer_type_ids = fields.Many2many(
        string="Supported Customer Types",
        comodel_name="res.partner.customer.type",
        columns2="website_acquirer_ids",
        help="Customer Types having this Acquirer enabled",
    )
