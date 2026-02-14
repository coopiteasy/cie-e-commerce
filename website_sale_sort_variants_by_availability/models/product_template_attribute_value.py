# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import api, fields, models


class ProductTemplateAttributeValue(models.Model):
    _inherit = "product.template.attribute.value"
    # the sale.variants template (used by default on the website product page)
    # lists records of this model in its default order. to control the order,
    # we change it here. another option would be to change the way the records
    # are accessed in the template, but that wouldn't be enough, because the
    # default order also controls which values are selected by default.
    #
    # since this represents only the value of an attribute and not a product,
    # it can only have an availability itself if the product template using it
    # is only using one attribute. when multiple attributes are used on a
    # product template, we should order them while also taking the other
    # attribute values into account. therefore, we sort by descending number
    # of available variants (products).
    _order = "available_variants_count desc, attribute_line_id, product_attribute_value_id, id"

    available_variants_count = fields.Integer(
        compute="_compute_available_variants_count", store=True
    )

    @api.depends("ptav_product_variant_ids.qty_available")
    def _compute_available_variants_count(self):
        for rec in self:
            rec.available_variants_count = sum(
                1
                for product in rec.ptav_product_variant_ids
                if product.qty_available > 0
            )
