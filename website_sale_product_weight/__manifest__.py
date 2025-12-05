# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

{
    "name": "Website Sale Product Weight",
    "summary": "Display the weight of a product on the e-commerce product page",
    "version": "16.0.1.0.0",
    "category": "Website",
    "website": "https://coopiteasy.be",
    "author": "Coop IT Easy SC",
    "license": "AGPL-3",
    "depends": [
        "website_sale",
    ],
    "data": [
        "views/templates.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "website_sale_product_weight/static/src/**/*",
        ],
    },
}
