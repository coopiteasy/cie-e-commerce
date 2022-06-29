# Copyright 2021 Coop IT Easy SC <http://coopiteasy.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Website Auto Publish',
    'summary': """Base module for automatic (un)publishing""",
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    "category": "Website",
    'author': 'Coop IT Easy SC <https://coopiteasy.be>',
    'website': 'https://github.com/coopiteasy/cie-e-commerce',
    'depends': [
        "website",
    ],
    'data': [
        "templates/website_navbar_templates.xml",
    ],
    'installable': True,
}
