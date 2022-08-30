
<!-- /!\ Non OCA Context : Set here the badge of your runbot / runboat instance. -->
[![Pre-commit Status](https://github.com/coopiteasy/cie-e-commerce/actions/workflows/pre-commit.yml/badge.svg?branch=12.0)](https://github.com/coopiteasy/cie-e-commerce/actions/workflows/pre-commit.yml?query=branch%3A12.0)
[![Build Status](https://github.com/coopiteasy/cie-e-commerce/actions/workflows/test.yml/badge.svg?branch=12.0)](https://github.com/coopiteasy/cie-e-commerce/actions/workflows/test.yml?query=branch%3A12.0)
[![codecov](https://codecov.io/gh/coopiteasy/cie-e-commerce/branch/12.0/graph/badge.svg)](https://codecov.io/gh/coopiteasy/cie-e-commerce)
<!-- /!\ Non OCA Context : Set here the badge of your translation instance. -->

<!-- /!\ do not modify above this line -->

# E-commerce modules

Modules aiming to support e-commerce-specific needs. This includes all the new website_sale-related modules included in version 12.0.

<!-- /!\ do not modify below this line -->

<!-- prettier-ignore-start -->

[//]: # (addons)

Available addons
----------------
addon | version | maintainers | summary
--- | --- | --- | ---
[website_auto_publish](website_auto_publish/) | 12.0.1.0.0 |  | Base module for automatic (un)publishing
[website_sale_add_to_cart_popup](website_sale_add_to_cart_popup/) | 12.0.1.0.0 |  | Always show the add to cart popup in the e-commerce.
[website_sale_close](website_sale_close/) | 12.0.1.0.0 |  | Allow to close the website for a moment and reopen it when needed.
[website_sale_customer_type](website_sale_customer_type/) | 12.0.1.0.0 |  | Let customer choose his type when accessing the e-commerce
[website_sale_delivery_product_restriction](website_sale_delivery_product_restriction/) | 12.0.1.0.0 |  | Allow some product to be shipped only by some delivery carrier and also on eCommerce.
[website_sale_product_sort_recent_arrival](website_sale_product_sort_recent_arrival/) | 12.0.1.0.0 |  | Let sort product on e-commerce by most recent arrival date.
[website_sale_stock_auto_publish](website_sale_stock_auto_publish/) | 12.0.1.0.0 |  | Allows the automatic (un)publishing of products according to the stock level


Unported addons
---------------
addon | version | maintainers | summary
--- | --- | --- | ---
[website_sale_customer_type_payment](website_sale_customer_type_payment/) | 12.0.1.0.0 (unported) |  | Restrict acquirers that a Customer Type can use on the e-commerce.
[website_sale_customer_type_signup](website_sale_customer_type_signup/) | 12.0.1.0.0 (unported) |  | Restrict Customer Type Signup on E-commerce

[//]: # (end addons)

<!-- prettier-ignore-end -->

## Licenses

This repository is licensed under [AGPL-3.0](LICENSE).

However, each module can have a totally different license, as long as they adhere to Coop IT Easy SC
policy. Consult each module's `__manifest__.py` file, which contains a `license` key
that explains its license.

----
<!-- /!\ Non OCA Context : Set here the full description of your organization. -->
