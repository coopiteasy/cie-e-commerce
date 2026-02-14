# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    def _get_possible_variants_sorted(self, parent_combination=None):
        # this is used by the website_sale.product_variants, which is not used
        # by default, but can be enabled by navigating to a product page on
        # the website, clicking edit, and in the customize tab, select
        # variants: products list. this only affects product templates that
        # use only one variant attribute; the other ones still use the default
        # template.
        self.ensure_one()
        return (
            super()
            ._get_possible_variants_sorted(parent_combination)
            # sudo is needed because public users don't have access to
            # stock.warehouse records.
            .sudo()
            .sorted(lambda product: product.qty_available > 0, reverse=True)
        )
