# Copyright 2021 Coop IT Easy SC <http://coopiteasy.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class WebsitePublishedMixin(models.AbstractModel):
    _inherit = "website.published.mixin"

    auto_managed_publishing = fields.Boolean(
        string="Managed Publishing",
        help="Enable the automatic (un)publishing",
    )

    @api.model
    def create(self, values):
        record = super().create(values)
        record.website_auto_publish()
        return record

    def write(self, values):
        res = super().write(values)
        self.website_auto_publish()
        return res

    def auto_publishing_value(self):
        """This method should be overridden with the automatic publishing
        rules."""
        self.ensure_one()
        return self.website_published

    def website_auto_publish(self):
        for record in self:
            if (
                record.auto_managed_publishing
                and record.auto_publishing_value() != record.website_published
            ):
                record.website_published = not record.website_published

    def website_publish_button(self):
        self.ensure_one()
        if not self.auto_managed_publishing:
            return super().website_publish_button()
        raise UserError(_("Automatic (un)publishing is enabled."))
