# Copyright 2021 Coop IT Easy SCRLfs <http://coopiteasy.be>
#   Rémy Taymans <remy@coopiteasy.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, exceptions, fields, models


class ResPartner(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"

    customer_type_id = fields.Many2one(
        comodel_name="res.partner.customer.type",
        string="Customer Type",
        help=(
            "Customer type used to distinguish different type of customer"
        )
    )
    website_restrict_product = fields.Boolean(
        string="Restrict Product on E-commerce",
        compute="_compute_website_restrict_product"
    )
    website_product_ids = fields.Many2many(
        comodel_name="product.template",
        string="Product",
        compute="_compute_website_product_ids",
    )

    def get_customer_type_id(self):
        """
        Return customer_type of the current partner and if empty
        check the customer_type of the commercial_partner_id.
        """
        self.ensure_one()
        return (
            self.customer_type_id
            or self.commercial_partner_id.customer_type_id
        )

    @api.depends("customer_type_id")
    def _compute_website_restrict_product(self):
        """
        Set website_restrict_product to True if the customer type
        has the flag website_restrict_product set.
        """
        for partner in self:
            partner.website_restrict_product = (
                partner.get_customer_type_id()
                and partner.get_customer_type_id().website_restrict_product
            )

    @api.depends("customer_type_id")
    def _compute_website_product_ids(self):
        """
        Return the list of product that can be seen on the e-commerce by
        the partner if connected depending on its customer type.
        """
        for partner in self:
            products = self.env["product.template"]
            if (
                partner.get_customer_type_id()
                and partner.get_customer_type_id().website_product_ids
            ):
                products |= partner.get_customer_type_id().website_product_ids
            partner.website_product_ids = products
