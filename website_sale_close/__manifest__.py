# Copyright 2019 Coop IT Easy SC
#   - Rémy Taymans <remy@coopiteasy.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Website Sale Close",
    "summary": """
        Allow to close the website for a moment and reopen it when needed.""",
    "version": "12.0.1.0.0",
    "license": "AGPL-3",
    "author": "Coop IT Easy SC",
    "website": "https://coopiteasy.be",
    "depends": [
        "website_sale",
        "website_payment",
    ],
    "data": [
        "views/res_config_settings.xml",
        "views/website.xml",
        "templates/website_sale_close.xml",
    ],
    "demo": [],
}
