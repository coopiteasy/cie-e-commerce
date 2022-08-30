# SPDX-FileCopyrightText: 2022 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

{
    "name": "Website Sale Private Product Page",
    "summary": """
        Allow users to access an e-commerce product page via a private URL even
        when the product is not published.""",
    "version": "12.0.1.0.0",
    "category": "Website",
    "website": "https://coopiteasy.be",
    "author": "Coop IT Easy SC",
    "maintainers": ["carmenbianca"],
    "license": "AGPL-3",
    "application": False,
    "depends": [
        "website_sale",
        "product",
    ],
    "excludes": [],
    "data": [
        "security/website_sale_private_product_page.xml",
        "data/actions.xml",
        "views/product_template_views.xml",
    ],
    "demo": [],
    "qweb": [],
}
