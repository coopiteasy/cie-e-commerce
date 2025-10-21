/** @odoo-module **/

/* Copyright CoopITEasy - Simon Hick <sim@coopiteasy.be>
   License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl) */

import {OptionalProductsModal} from "@sale_product_configurator/js/product_configurator_modal";

OptionalProductsModal.include({
    init() {
        this._super.apply(this, arguments);
        this.forceDialog = true;
    },
});
