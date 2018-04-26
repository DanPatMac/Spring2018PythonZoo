# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Zoo, Exhibit, Neighbors

# Register your models here.

class ZooAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

admin.site.register(Zoo, ZooAdmin)

class ExhibitAdmin(admin.ModelAdmin):
    list_display = ("id", "name") 

admin.site.register(Exhibit, ExhibitAdmin)   

class NeighborsAdmin(admin.ModelAdmin):
    list_display = ("id", "toExhibit")

admin.site.register(Neighbors, NeighborsAdmin)
