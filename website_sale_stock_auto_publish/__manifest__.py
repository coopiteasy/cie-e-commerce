# Copyright 2021 Coop IT Easy SC <http://coopiteasy.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Website Sale Stock Auto Publish",
    "summary": """
        Allows the automatic (un)publishing of products according to the stock
        level
    """,
    "version": "12.0.1.0.0",
    "license": "AGPL-3",
    "category": "Website",
    "author": "Coop IT Easy SC",
    "website": "https://coopiteasy.be",
    "depends": [
        "website_auto_publish",
        "website_sale_stock",
    ],
    "data": [
        "views/product_template_views.xml",
    ],
    "installable": True,
}
