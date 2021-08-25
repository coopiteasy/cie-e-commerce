Product Restriction
~~~~~~~~~~~~~~~~~~~

To restrict products that a user can see on the e-commerce an Customer
Type should be assigned to the partner associated with the User used by
the customer. If this partner is a contact of a company, the Customer
Type should be assigned to the company.

Then on the Customer Type, the `website_restrict_product` field should
be set to `True` **and** the field `website_product_ids` should be
filled with some products. When the `website_restrict_product` is set,
the only product that this user will see will be the one in the
`website_product_ids` list. If this list is empty, the user will see no
product on the e-commerce.

To assign product to a Customer Type, it can also be done by adding the
Customer Type directly on the Product form under the *Website
Restriction* topic.

!Waring! The product are filtered on the e-commerce **only** if the
customer is logged in !

eCommerce Categories Restriction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To restrict eCommerce Categories that a user can see on the e-commerce,
a Customer Type should be assigned to the partner associated with the
User used by the customer. If this partner is a contact of a company,
the Customer Type should be assigned to the company.

Then on the Customer Type, the `website_restrict_public_categ` field
should be set to `True` **and** the field `website_public_categ_ids`
should be filled with some categories.
When the `website_restrict_public_categ` is set, the only category that
this user will see will be the one in the `website_public_categ_ids` list.
If this list is empty, the user will see no category on the e-commerce.

To assign category to a Customer Type, it can also be done by adding the
Customer Type directly on the eCommerce Categories form under the
*Website Restriction* topic.

!Warning! The categories are filtered on the e-commerce **only** if the
customer is logged in !


Customer Type Selector
~~~~~~~~~~~~~~~~~~~~~~

By default, this module don't show a Customer Selector on the
e-commerce. The goal of the Customer Selector is to let the user choose
his type of customer a be guided to the right procedure to connect.

Customer Type can be configured under *Contacts > Configuration >
Customer Type*.

To enable the Customer Selector on the e-commerce, it must exists at
least one Customer Type with the *Show On Website* property set to True.


Acquirer Restriction
~~~~~~~~~~~~~~~~~~~~

On the Customer Type, the `website_restrict_acquirer` field should
be set to `True` **and** the field `website_acquirer_ids` should be
filled with some acquirers. When the `website_restrict_acquirer` is set,
the only acquirer that this user will see will be the one in the
`website_acquirer_ids` list. If this list is empty, the user will see all
activated/published acquirers.

To assign acquirer to a Customer Type, it can also be done by adding the
Customer Type directly on the Payment Acquirer form under the *Configuration* tab.
