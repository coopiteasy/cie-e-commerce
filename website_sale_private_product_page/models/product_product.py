# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import models


class ProductProduct(models.Model):
    _inherit = "product.product"

    def action_generate_private_url_token(self):
        self.product_tmpl_id.action_generate_private_url_token()

    def action_clear_private_url_token(self):
        self.product_tmpl_id.action_clear_private_url_token()
