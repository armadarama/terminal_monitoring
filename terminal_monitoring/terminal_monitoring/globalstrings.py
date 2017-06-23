from django.utils import translation

# Translates message and returns it in a unicode string
from django.utils.translation import ugettext_lazy as _

#Translates singular and plural and returns the appropriate string based on number in a unicode string.
from django.utils.translation import ungettext 

from django.utils.translation import activate, get_language


class Globalstrings(object): 
	employee = _('Employee')
	online = _('Online')
	offline5lower = _('Offline5lower')
	offline5greater = _('Offline5greater')