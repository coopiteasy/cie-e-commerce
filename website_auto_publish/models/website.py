# Copyright 2021 Coop IT Easy SCRLfs <http://coopiteasy.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class WebsitePublishedMixin(models.AbstractModel):
    _inherit = 'website.published.mixin'

    auto_managed_publishing = fields.Boolean(
        string="Managed Publishing",
        help="Enable the automatic (un)publishing",
    )

    @api.model
    def create(self, values):
        record = super(WebsitePublishedMixin, self).create(values)
        record.website_auto_publish()
        return record

    @api.multi
    def write(self, values):
        res = super(WebsitePublishedMixin, self).write(values)
        self.website_auto_publish()
        return res

    def auto_publishing_value(self):
        """This method should be overridden with the automatic publishing
        rules."""
        self.ensure_one()
        return self.website_published

    @api.multi
    def website_auto_publish(self):
        for record in self:
            if record.auto_managed_publishing and \
               record.auto_publishing_value() != record.website_published:
                record.website_published = not record.website_published

    @api.multi
    def website_publish_button(self):
        self.ensure_one()
        if not self.auto_managed_publishing or (self.website_url != '#' and
           self.env.user.has_group('website.group_website_publisher')):
            return super(WebsitePublishedMixin, self).website_publish_button()
        raise UserError(_("Automatic (un)publishing is enabled."))
