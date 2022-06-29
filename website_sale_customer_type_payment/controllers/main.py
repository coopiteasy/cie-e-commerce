# Copyright 2021 Coop IT Easy SC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, http
from odoo.http import request
from odoo.addons.website_sale_customer_type.controllers.main import (
    WebsiteSale as Base
)


class WebsiteSale(Base):

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
