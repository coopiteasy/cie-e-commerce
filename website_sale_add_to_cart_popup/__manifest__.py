# Copyright 2021 Coop IT Easy SCRLfs <https://coopiteasy.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Website Sale Add To Cart Popup",
    "summary": "Always show the add to cart popup in the e-commerce.",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "author": "Coop IT Easy SC",
    "website": "https://coopiteasy.be",
    "depends": [
        "sale_product_configurator",
        "website_sale",
    ],
    "assets": {
        "web.assets_frontend": [
            "website_sale_add_to_cart_popup/static/src/js/product_configurator_modal.esm.js",
        ],
    },
}
