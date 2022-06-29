# Copyright 2021 Coop IT Easy SC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, http
from odoo.http import request
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.addons.website_sale_customer_type.controllers.main import (
    WebsiteSale as Base
)
from odoo.exceptions import UserError


class AuthSignupHome(AuthSignupHome):

    @http.route('/web/signup', type='http', auth='public', website=True)
    def web_auth_signup(self, customer_type=None, *args, **kw):
        """Handles `customer_type` argument as an URL parameter.
        URL parameter has priority on request.session.
        """
        response = super(AuthSignupHome, self).web_auth_signup(*args, **kw)
        if not customer_type and response.qcontext.get('customer_type'):
            return response
        res_partner_customer_type = False
        if customer_type and customer_type.isdigit() and int(customer_type) >= 0:
            customer_type_id = int(customer_type)  # parameter is interpreted as a str
            res_partner_customer_type = request.env["res.partner.customer.type"].sudo().browse(customer_type_id)
        response.qcontext.update({
            'customer_type': res_partner_customer_type
        })
        return response

    def get_auth_signup_qcontext(self):
        """Handles customer_type stored in request.session.
        This function is called in web_auth_signup()
        """
        qcontext = super(AuthSignupHome, self).get_auth_signup_qcontext()
        qcontext["is_signup"] = (
            "/web/signup" == request.httprequest.path
        )
        if "customer_type" not in qcontext:
            qcontext["customer_type"] = (
                request.env["res.partner.customer.type"]
                .sudo()
                .browse(request.session.get("customer_type"))
                .exists()
            )
        return qcontext

    def do_signup(self, qcontext):
        """Shared helper that creates a res.partner out of a token.
        Taken from odoo/addons/auth_signup/controllers/main.py and adapted for cet_website_sale.
        Attention: breaks the inheritance mechanism.
        """
        # Determine required fields
        required_fields = ["login", "name", "password"]
        if qcontext["is_signup"]:
            required_fields.append("customer_type")
            required_fields.append("customer_type_id")
        values = dict((key, qcontext.get(key)) for key in required_fields)
        if not all([key for key in values.values()]):
            raise UserError(_("The form was not properly filled in."))

        if qcontext["is_signup"]:
            try:
                customer_type_id_int = int(values.get("customer_type_id"))
            except (ValueError, TypeError) as err:
                raise UserError(err)
            customer_type_id = (
                request.env["res.partner.customer.type"]
                .sudo()
                .browse(customer_type_id_int)
                .exists()
            )
            if not customer_type_id:
                raise UserError(_("This Customer Type does not exists."))
            if customer_type_id.website_restrict_signup:
                raise UserError("%s" % customer_type_id.website_restrict_signup_text)
            if customer_type_id.website_signup_vat_required:
                if not qcontext.get('vat'):
                    raise UserError("%s" % customer_type_id.website_signup_vat_required_text)
                values['vat'] = qcontext.get('vat')

        if values.get('password') != qcontext.get('confirm_password'):
            raise UserError(_("Passwords do not match; please retype them."))
        supported_langs = [lang['code'] for lang in request.env['res.lang'].sudo().search_read([], ['code'])]
        if request.lang in supported_langs:
            values['lang'] = request.lang
        self._signup_with_values(qcontext.get('token'), values)
        request.env.cr.commit()


class WebsiteSale(Base):

    def _get_mandatory_billing_fields(self):
        result = super(WebsiteSale, self)._get_mandatory_billing_fields()
        if "customer_type" in request.session:
            customer_type_id = (
                request
                    .env["res.partner.customer.type"]
                    .sudo()
                    .browse(int(request.session["customer_type"]))
            )
            if customer_type_id.website_signup_vat_required:
                result.append("vat")
        return result

    @http.route(['/shop/address'], type='http', methods=['GET', 'POST'], auth="public", website=True, sitemap=False)
    def address(self, **kw):
        result = super(WebsiteSale, self).address(**kw)
        if "customer_type" in request.session:
            result.qcontext["customer_type"] = (
                result.qcontext.get("customer_type") or
                request.env["res.partner.customer.type"].sudo().browse(int(request.session["customer_type"]))
                )
        return result
