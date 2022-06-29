# Copyright 2021 Coop IT Easy SC <https://coopiteasy.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Website Sale Customer Type',
    'summary': """
        Let customer choose his type when accessing the e-commerce""",
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Coop IT Easy SC <https://coopiteasy.be>',
    'website': 'https://github.com/coopiteasy/cie-e-commerce',
    'depends': [
        "contacts",
        "website_sale",
    ],
    'data': [
        "views/product.xml",
        "views/res_partner.xml",
        "views/res_partner_customer_type.xml",
        "views/website_sale_templates.xml",
        "security/ir.model.access.csv",
    ],
    'demo': [
    ],
}
