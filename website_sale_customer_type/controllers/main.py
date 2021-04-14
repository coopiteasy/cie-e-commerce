# Copyright 2018 Coop IT Easy SCRLfs
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, http
from odoo.http import request
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.addons.website_sale.controllers.main import (
    PPG, TableCompute, WebsiteSale as Base
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

    def _user_can_shop(self):
        """
        Return True if the user can shop or False if it needs to follow
        the customer selector process.
        """
        customer_type_id = None
        user_customer_type_id = (
            request.env.user.partner_id.get_customer_type_id()
        )
        if "customer_type" in request.session:
            customer_type_id = (
                request
                .env["res.partner.customer.type"]
                .sudo()
                .browse(int(request.session["customer_type"]))
            )
        return (
            request.session["uid"]
            and customer_type_id
            and customer_type_id == user_customer_type_id
        ) or (
            not request.session["uid"]
            and customer_type_id
            and not customer_type_id.website_require_early_login
        )

    def _get_customer_selector_vals(self):
        """
        Return values for the template that generate de popover
        selector.
        """
        vals = {}
        customer_type_ids = (
            request
            .env["res.partner.customer.type"]
            .sudo()
            .search(
                [("show_on_website", "=", True)]
            )
        )
        vals["show_customer_type_selector"] = (
            customer_type_ids and not self._user_can_shop()
        )
        vals["customer_type_ids"] = customer_type_ids
        if "customer_type_selector_error" in request.session:
            vals["customer_type_selector_error"] = request.session[
                "customer_type_selector_error"
            ]
        return vals

    def _is_product_allowed(self, product_tmpl, allowed_products):
        """
        Return True if the product_tmpl is allowed based on the
        allowed_products list.
        product_tmpl must be a product.template.
        """
        # TODO: Validate this when product_variant is not activate !
        for variant in product_tmpl.product_variant_ids:
            if allowed_products is not None and variant in allowed_products:
                return True
            elif allowed_products is None:
                return True
        return False

    @http.route(
        ['/set/customer_type'], type='http', auth="public", website=True
    )
    def set_customer_type(self, customer_type=None, origin_url=None, **post):
        """
        Set the customer_type in the request.session and redirect to
        next_url.
        """
        # Remove previous error if any
        if "customer_type_selector_error" in request.session:
            del request.session["customer_type_selector_error"]

        customer_type_id = (
            request
            .env["res.partner.customer.type"]
            .sudo()
            .browse(int(customer_type))
        )

        # Set customer_type in session
        request.session["customer_type"] = customer_type_id.id

        # Redirect
        next_url = (
            "/check/customer_type?next_url=%s&origin_url=%s"
            % (customer_type_id.next_url or origin_url, origin_url)
        )
        if customer_type_id.website_require_early_login:
            return request.redirect("/web/login?redirect=%s" % next_url)
        return request.redirect(next_url)

    @http.route(
        ['/check/customer_type'], type='http', auth="public", website=True
    )
    def check_customer_type(self, origin_url=None, next_url=None, **post):
        """
        Check if the customer type choice is correct regarding to the
        connected user.
        """
        # Check that customer type is in session to test this choice
        if "customer_type" not in request.session:
            return request.redirect(origin_url)
        customer_type_id = (
            request
            .env["res.partner.customer.type"]
            .sudo()
            .browse(int(request.session["customer_type"]))
        )
        # Check state that needs to show errors to the user
        partner = request.env.user.partner_id
        if (
            customer_type_id.website_require_early_login
            or request.session["uid"]
        ) and partner.get_customer_type_id() != customer_type_id:
            request.session.logout(keep_db=True)
            request.session["customer_type_selector_error"] = _(
                "Mismatch between the customer type selected and the "
                "customer type of the user. Please select a customer "
                "type and login with the corresponding user."
            )
            return request.redirect(origin_url)
        if not self._user_can_shop():
            return request.redirect(origin_url)
        return request.redirect(next_url)

    @http.route()
    def shop(self, page=0, category=None, search="", ppg=False, **post):
        """
        This function overwrite the shop function to filter the product
        that will be shown on this page. As the amount of product will
        be different than in the original function, page number should
        be recalculated.
        """
        # Set product per page
        if ppg:
            try:
                ppg = int(ppg)
            except ValueError:
                ppg = PPG
        else:
            ppg = PPG

        # Call the parent function and get all of the products
        response = super().shop(
            page=0,
            category=category,
            search=search,
            ppg='10000',
            **post
        )
        products = response.qcontext["products"]

        # Get current user list of products (product.product)
        if request.env.user.website_restrict_product:
            allowed_products = request.env.user.website_product_ids
        else:
            allowed_products = None

        # Filter products
        products = products.filtered(
            lambda p: self._is_product_allowed(p, allowed_products)
        )

        # Construct pager
        keep = response.qcontext["keep"]
        product_count = len(products.ids)
        post.update({key: val for key, val in keep.args.items() if val})
        pager = request.website.pager(
            url=keep.path,
            total=product_count,
            page=page,
            step=ppg,
            scope=7,
            url_args=post
        )

        # Truncate product according to the pager
        products = products[pager["offset"]:pager["offset"] + ppg]

        # Add element to context
        response.qcontext["products"] = products
        response.qcontext["restrict_product"] = (
            request.env.user.website_restrict_product
        )
        response.qcontext["allowed_products"] = allowed_products
        response.qcontext["product_count"] = product_count
        response.qcontext["pager"] = pager
        response.qcontext["bins"] = TableCompute().process(products, ppg)
        response.qcontext.update(self._get_customer_selector_vals())
        return response

    @http.route()
    def product(self, product, category="", search="", **kwargs):
        response = super().product(product, category, search, **kwargs)

        # Get product list allowed for the current user (product.product)
        if request.env.user.website_restrict_product:
            allowed_products = request.env.user.website_product_ids
        else:
            allowed_products = None

        # Filter alternative_product_ids
        if allowed_products is not None:
            allowed_product_tmpls = allowed_products.mapped("product_tmpl_id")
            alt_product_ids = product.alternative_product_ids.filtered(
                lambda p: p in allowed_product_tmpls
            )
        else:
            alt_product_ids = product.alternative_product_ids
        response.qcontext["alt_product_ids"] = alt_product_ids
        return response

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

    def _get_shop_payment_values(self, order, **kwargs):
        result = super(WebsiteSale, self)._get_shop_payment_values(
            order, **kwargs
        )
        shipping_partner_id = False
        if order:
            shipping_partner_id = (
                order.partner_shipping_id.id or order.partner_invoice_id.id
            )
        allowed_acquirers = {}
        if request.env.user.website_restrict_acquirer:
            allowed_acquirers = request.env.user.website_acquirer_ids

        form_acquirers = [
            acq
            for acq in allowed_acquirers
            if acq.payment_flow == "form" and acq.view_template_id
        ]
        s2s_acquirers = [
            acq
            for acq in allowed_acquirers
            if acq.payment_flow == "s2s" and acq.registration_view_template_id
        ]

        for acq in form_acquirers:
            acq.form = (
                acq.with_context(
                    submit_class="btn btn-primary", submit_txt=_("Pay Now")
                )
                    .sudo()
                    .render(
                    "/",
                    order.amount_total,
                    order.pricelist_id.currency_id.id,
                    values={
                        "return_url": "/shop/payment/validate",
                        "partner_id": shipping_partner_id,
                        "billing_partner_id": order.partner_invoice_id.id,
                    },
                )
            )

        if form_acquirers:
            result["form_acquirers"] = form_acquirers
        if s2s_acquirers:
            result["s2s_acquirers"] = s2s_acquirers

        return result
