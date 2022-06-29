# Copyright 2021 Coop IT Easy SC <http://coopiteasy.be>
#   Rémy Taymans <remy@coopiteasy.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, exceptions, fields, models


class ResPartner(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"

    website_restrict_acquirer = fields.Boolean(
        string="Restrict Acquirer on E-commerce",
        compute="_compute_website_restrict_acquirer"
    )
    website_acquirer_ids = fields.Many2many(
        comodel_name="payment.acquirer",
        string="Acquirer",
        compute="_compute_website_acquirer_ids",
    )

    @api.depends("customer_type_id")
    def _compute_website_restrict_acquirer(self):
        """
        Set website_restrict_acquirer to True if the customer type
        has the flag website_restrict_acquirer set.
        """
        for partner in self:
            partner.website_restrict_acquirer = (
                partner.get_customer_type_id()
                and partner.get_customer_type_id().website_restrict_acquirer
            )

    @api.depends("customer_type_id")
    def _compute_website_acquirer_ids(self):
        """
        Return the list of acquirer that can be seen on the e-commerce by
        the partner if connected depending on its customer type.
        """
        for partner in self:
            acquirers = self.env["payment.acquirer"]
            if (
                partner.get_customer_type_id()
                and partner.get_customer_type_id().website_acquirer_ids
            ):
                acquirers |= partner.get_customer_type_id().website_acquirer_ids
            partner.website_acquirer_ids = acquirers
