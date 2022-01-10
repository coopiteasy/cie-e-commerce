This module completely shuts down the webshop with a configurable message.

This module is principally incompatible with other modules that override public
functions in the website_sale controller. If this module is loaded before the
second module, that module will most likely raise an exception because of a
malformed response object from this module. There exists---to my best
knowledge---no way to make sure that this module is always loaded last.
