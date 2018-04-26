# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Zoo(models.Model):
    name = models.CharField(max_length=200, help_text="Enter Zoo Name")
    
    def __str__(self):
        return self.name
class Exhibit(models.Model):
    name = models.CharField(max_length=200, help_text="Enter Exhibit Name")
    zoo = models.ForeignKey("Zoo", on_delete=models.SET_NULL, null=True)
    hasExit = models.BooleanField(default=False)

    def __str__(self):
        return self.name
class Neighbors(models.Model):
    fromExhibit = models.ForeignKey("Exhibit", on_delete=models.SET_NULL, null=True, related_name='fromExhibit')
    direction = models.CharField(max_length=2, help_text="Enter Direction To Travel")
    toExhibit = models.ForeignKey("Exhibit", on_delete=models.SET_NULL, null=True, related_name='toExhibit')

    def __str__(self):
        return self.direction
