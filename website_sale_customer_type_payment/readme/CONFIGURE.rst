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
