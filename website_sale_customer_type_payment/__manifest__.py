# Copyright 2021 Coop IT Easy SC <https://coopiteasy.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Website Sale Customer Type Payment',
    'summary': """
        Restrict acquirers that a Customer Type can use on the e-commerce.""",
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Coop IT Easy SC <https://coopiteasy.be>',
    'website': 'https://coopiteasy.be',
    'depends': [
        "website_sale_customer_type",
    ],
    'data': [
        "views/payment_views.xml",
        "views/res_partner_customer_type.xml",
    ],
    'demo': [
    ],
    'installable': False,  # not tested
}
