# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
# Create your models here.

class Zoo(models.Model):
    name = models.CharField(max_length=200, help_text="Enter Zoo Name")
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('zooDetail', args=[str(self.id)])

class Exhibit(models.Model):
    name = models.CharField(max_length=200, help_text="Enter Exhibit Name")
    zoo = models.ForeignKey("Zoo", on_delete=models.SET_NULL, null=True, related_name='parentZoo')
    hasExit = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('exhibitDetail', args=[str(self.id)])

class Neighbors(models.Model):
    fromExhibit = models.ForeignKey("Exhibit", on_delete=models.SET_NULL, null=True, related_name='fromExhibit')
    direction = models.CharField(max_length=2, help_text="Enter Direction To Travel")
    toExhibit = models.ForeignKey("Exhibit", on_delete=models.SET_NULL, null=True, related_name='toExhibit')

    def __str__(self):
        return self.direction

class Animals(models.Model):
    parentExhibit = models.ForeignKey("Exhibit", on_delete=models.SET_NULL, null=True, related_name='parentExhibit')
    name = models.CharField(max_length=200, help_text="Enter Animal Name", null=True)
    imageFilePath = models.CharField(max_length=200, help_text="Enter Image Path", null=True)
    soundFilePath = models.CharField(max_length=200, help_text="Enter Sound Path", null=True)
    habitatDesc = models.TextField(max_length=1000, help_text="Enter a Description", null=True)
    dietDesc = models.TextField(max_length=1000, help_text="Enter a Description", null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('animalDetail', args=[str(self.id)])

