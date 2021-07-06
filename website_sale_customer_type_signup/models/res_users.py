from odoo import api, models, _
from odoo.addons.auth_signup.models.res_partner import SignupError


class ResUsers(models.Model):
    _inherit = "res.users"

    @api.model
    def _signup_create_user(self, values):
        """sets `customer_type_id` to the new user created from the template user"""
        if 'customer_type' not in values:
            raise SignupError(_("Signup: customer type is required"))

        res_partner_customer_type = (
            self.env["res.partner.customer.type"]
                .sudo()
                .search([("name", "=", values.get("customer_type"))])
        )
        if not res_partner_customer_type:
            raise SignupError(_("Signup: this customer type does not exist"))
        if res_partner_customer_type.website_restrict_signup:
            raise SignupError("%s" % res_partner_customer_type.website_restrict_signup_text)
        if res_partner_customer_type.website_signup_vat_required:
            if 'vat' not in values:
                raise SignupError("%s" % res_partner_customer_type.website_signup_vat_required_text)
        template_user = super(ResUsers, self)._signup_create_user(values)
        template_user.write({"customer_type_id": res_partner_customer_type.id})
        return template_user
