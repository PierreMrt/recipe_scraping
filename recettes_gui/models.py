from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    difficulty = models.CharField(max_length=255, null=True, blank=True)
    cost = models.CharField(max_length=255, null=True, blank=True)
    prep_time = models.CharField(max_length=255, null=True, blank=True)
    cook_time = models.CharField(max_length=255, null=True, blank=True)
    ingredients = models.TextField(null=True, blank=True)
    steps = models.TextField(null=True, blank=True)


