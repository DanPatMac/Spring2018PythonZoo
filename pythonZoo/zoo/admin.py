# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Zoo, Exhibit, Neighbors, Animals

# Register your models here.

class ZooAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "get_absolute_url")

admin.site.register(Zoo, ZooAdmin)

class ExhibitAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "get_absolute_url") 

admin.site.register(Exhibit, ExhibitAdmin)   

class NeighborsAdmin(admin.ModelAdmin):
    list_display = ("id", "toExhibit")

admin.site.register(Neighbors, NeighborsAdmin)

class AnimalsAdmin(admin.ModelAdmin):
    list_display = ("id", "name","imageFilePath","soundFilePath","habitatDesc","dietDesc","get_absolute_url")

admin.site.register(Animals, AnimalsAdmin)
