# Copyright 2019-Today Coop IT Easy SC
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests.common import HttpCase


class WebsiteSaleCloseCase(HttpCase):
    def test_01_check_e_commerce_open(self):
        website = self.env["website"].browse(1)
        website.is_ecommerce_open = True
        result = self.url_open("/shop")
        self.assertNotIn(website.text_closed_ecommerce, result.text)
        result = self.url_open("/shop/cart")
        self.assertNotIn(website.text_closed_ecommerce, result.text)
        result = self.url_open("/shop/checkout")
        self.assertNotIn(website.text_closed_ecommerce, result.text)

    def test_02_check_e_commerce_close(self):
        website = self.env["website"].browse(1)
        website.is_ecommerce_open = False
        result = self.url_open("/shop")
        self.assertIn(website.text_closed_ecommerce, result.text)
        result = self.url_open("/shop/cart")
        self.assertIn(website.text_closed_ecommerce, result.text)
        result = self.url_open("/shop/checkout")
        self.assertIn(website.text_closed_ecommerce, result.text)
