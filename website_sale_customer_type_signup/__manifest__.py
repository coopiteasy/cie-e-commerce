# Copyright 2021 Coop IT Easy SC <https://coopiteasy.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Website Sale Customer Type Signup',
    'summary': """
        Restrict Customer Type Signup on E-commerce""",
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Coop IT Easy SC <https://coopiteasy.be>',
    'website': 'https://github.com/coopiteasy/cie-e-commerce',
    'depends': [
        "auth_signup",
        "website_sale_customer_type",
    ],
    'data': [
        "views/auth_signup_login_templates.xml",
        "views/portal_templates.xml",
        "views/res_partner_customer_type.xml",
        "views/website_sale_templates.xml",
    ],
    'demo': [
    ],
    'installable': False,  # not tested
}
