/** @odoo-module **/
// SPDX-FileCopyrightText: 2022 Coop IT Easy SC
//
// SPDX-License-Identifier: AGPL-3.0-or-later

import VariantMixin from "sale.VariantMixin";
import {WebsiteSale} from "website_sale.website_sale";
import {patch} from "@web/core/utils/patch";

VariantMixin._onChangeCombinationWeight = function (_ev, $parent, combination) {
    var $weight = $parent.find(".oe_product_weight:first .oe_product_weight_value");
    $weight.html(combination.weight);

    var $weight_uom_name = $parent.find(
        ".oe_product_weight:first .oe_product_weight_uom_name_value"
    );
    $weight_uom_name.html(combination.weight_uom_name);
};

patch(WebsiteSale.prototype, "website_sale_product_weight", {
    _onChangeCombination: function () {
        this._super.apply(this, arguments);
        VariantMixin._onChangeCombinationWeight.apply(this, arguments);
    },
});
