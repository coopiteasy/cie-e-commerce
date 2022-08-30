# Copyright 2021 Coop IT Easy SC <http://coopiteasy.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models


class ProductTemplate(models.Model):
    _name = "product.template"
    _inherit = ["product.template", "website.published.mixin"]

    def auto_publishing_value(self):
        self.ensure_one()
        value = super(ProductTemplate, self).auto_publishing_value()
        if self.inventory_availability == "always":
            value = self.virtual_available > 0
        elif self.inventory_availability == "threshold":
            value = self.virtual_available > self.available_threshold
        return value
