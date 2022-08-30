# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import psycopg2

from odoo.tests.common import SavepointCase
from odoo.tools import mute_logger


class TestProductTemplate(SavepointCase):
    def test_token_unique(self):
        """A token can only be used by one record."""
        product_1 = self.env["product.template"].create({"name": "Product 1"})
        product_1.private_url_token = "Foo"

        product_2 = self.env["product.template"].create({"name": "Product 2"})
        # Muting the logger because otherwise an ERROR will be printed to the
        # log, even though the error is expected.
        with self.assertRaises(psycopg2.IntegrityError), mute_logger("odoo.sql_db"):
            product_2.private_url_token = "Foo"

    def test_generate_token(self):
        """Token generation works."""
        product_1 = self.env["product.template"].create({"name": "Product 1"})
        self.assertFalse(product_1.private_url_token)
        product_1.action_generate_private_url_token()
        self.assertTrue(product_1.private_url_token)
        self.assertIsInstance(product_1.private_url_token, str)

    def test_clear_token(self):
        """Token clearing works."""
        product_1 = self.env["product.template"].create({"name": "Product 1"})
        product_1.private_url_token = "Foo"
        self.assertTrue(product_1.private_url_token)
        product_1.action_clear_private_url_token()
        self.assertIs(product_1.private_url_token, False)
