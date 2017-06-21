from django.contrib import admin

from django.contrib import admin
from .models import Accesspoint, Site, Terminal

admin.site.register(Accesspoint)
admin.site.register(Site)
admin.site.register(Terminal)

