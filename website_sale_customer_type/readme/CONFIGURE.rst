Customer Type
~~~~~~~~~~~~~

Customer Type can be configured under *Contacts > Configuration >
Customer Type*.


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


Customer Type for non-connected user
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, user that are not logged in on the e-commerce will have no
Customer Type. So no restriction will be applied.

To set a default Customer Type that applies on user that are not
connected on the e-commerce, do the following:

- Go to Configuration > Users
- Remove de default filter and select the filter "Inactive Users".
- Search for "Public" and select the "Public User".
- Click on the partner linked to this user.
- On the partner form set a Customer Type and save.

The Customer Type set on the "Public User" will be used for users that
are not connected to the e-commerce.
