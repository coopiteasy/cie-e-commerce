# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import secrets
import string

from odoo import api, fields, models

_LETTERS_AND_DIGITS = string.ascii_lowercase + string.digits


class ProductTemplate(models.Model):
    _inherit = "product.template"

    private_url_token = fields.Char(
        string="Private URL Token",
        help="""
            A randomly generated token that can be used by third parties to
            access the product's e-commerce page even when the product is not
            published. Make sure to keep the token secret from those whom you do
            not want to see the product page.""",
        readonly=True,
        copy=False,
    )
    private_url = fields.Char(
        string="Private URL",
        readonly=True,
        compute="_compute_private_url",
        store=True,
    )

    _sql_constraints = [
        (
            "private_url_token_unique",
            "UNIQUE (private_url_token)",
            "The private URL token must be unique",
        )
    ]

    @api.depends("private_url_token")
    def _compute_private_url(self):
        for template in self:
            if not template.private_url_token:
                template.private_url = False
            else:
                template.private_url = "/shop/private_product/{}".format(
                    template.private_url_token
                )

    def action_generate_private_url_token(self):
        count = len(self)
        while True:
            tokens = {self._generate_private_url_token() for _ in range(count)}
            # Check for a once-in-131_621_703_842_267_136 event: the same token
            # being generated twice.
            if len(tokens) != count or self.search(
                [("private_url_token", "in", list(tokens))]
            ):
                continue
            break
        for template in self:
            template.private_url_token = tokens.pop()

    def action_clear_private_url_token(self):
        for template in self:
            template.private_url_token = False

    def _generate_private_url_token(self):
        # 11-character string of random letters (both upper- and lowercase) and
        # digits. 11 was chosen because it's the length YouTube uses, which
        # ought to be plenty sufficient for uniqueness. Although YouTube also
        # uses uppercase letters.
        return "".join(secrets.choice(_LETTERS_AND_DIGITS) for _ in range(11))
