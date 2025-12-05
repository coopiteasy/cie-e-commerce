/** @odoo-module **/
// SPDX-FileCopyrightText: 2025 Coop IT Easy SC
//
// SPDX-License-Identifier: AGPL-3.0-or-later

import {patch} from "@web/core/utils/patch";
import {systrayItem} from "@website/systray_items/publish";
import {useService} from "@web/core/utils/hooks";

const {onWillStart, xml} = owl;

patch(systrayItem.Component.prototype, "AutoPublishSystray", {
    setup() {
        this._super(...arguments);
        this.ormService = useService("orm");

        onWillStart(async () => {
            const mainObject = this.website.currentWebsite.metadata.mainObject;
            const result = await this.ormService.read(
                mainObject.model,
                [mainObject.id],
                ["auto_managed_publishing"]
            );
            this.auto_managed_publishing = result[0].auto_managed_publishing;
        });
    },

    async publishContent() {
        if (this.auto_managed_publishing) {
            return;
        }
        return this._super(...arguments);
    },
});

// Unfortunately, it does not seem possible to modify a template defined using
// the xml helper, so we have to redefine it completely. The only changed
// parts here are in the top-level div's attributes:
// * Converting the class attribute to t-attf-class and adding the conditional
//   o_disabled class to it.
// * Converting the data-hotkey attribute to t-att-data-hotkey to set its
//   value conditionally.
systrayItem.Component.template = xml`
<div
    t-on-click="publishContent"
    t-attf-class="o_menu_systray_item d-md-flex ms-auto {{auto_managed_publishing and 'o_disabled'}}"
    t-att-data-hotkey="!auto_managed_publishing and 'p'"
    t-att-data-processing="state.processing and 1"
>
    <a href="#">
        <Switch value="state.published" disabled="true" extraClasses="'mb-0 o_switch_danger_success'"/>
        <span class="d-none d-md-block ms-2" t-esc="this.label"/>
    </a>
</div>`;
