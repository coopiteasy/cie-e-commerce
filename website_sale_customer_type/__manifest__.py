# Copyright 2020 Coop IT Easy SCRLfs <https://coopiteasy.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Website Sale Customer Type',
    'description': """
        Show different product and payement acquirer depending on the
        customer type assigned to a customer on the e-commerce.""",
    'version': '11.0.2.0.0',
    'license': 'AGPL-3',
    'author': 'Coop IT Easy SCRLfs <https://coopiteasy.be>',
    'website': 'https://github.com/coopiteasy/cie-e-commerce',
    'depends': [
        "contacts",
        "website_sale",
    ],
    'data': [
        "views/payment_views.xml",
        "views/product_product.xml",
        "views/res_partner.xml",
        "views/res_partner_customer_type.xml",
        "views/website_sale_templates.xml",
        "security/ir.model.access.csv",
    ],
    'demo': [
    ],
}
