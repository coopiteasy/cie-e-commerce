# Copyright 2021 Coop IT Easy SC <http://coopiteasy.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Website Auto Publish",
    "summary": "Base module for automatic (un)publishing",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "category": "Website",
    "author": "Coop IT Easy SC",
    "website": "https://coopiteasy.be",
    "depends": [
        "website",
    ],
    "assets": {
        "website.assets_editor": [
            "website_auto_publish/static/src/scss/website.scss",
            "website_auto_publish/static/src/systray_items/*.js",
        ],
    },
}
