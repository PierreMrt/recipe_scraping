from django.db import models
from lib.scraper import scrap_links, scrap_recipe

class Recipe(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    difficulty = models.CharField(max_length=255, null=True, blank=True)
    cost = models.CharField(max_length=255, null=True, blank=True)
    prep_time = models.CharField(max_length=255, null=True, blank=True)
    cook_time = models.CharField(max_length=255, null=True, blank=True)
    ingredients = models.TextField(null=True, blank=True)
    steps = models.TextField(null=True, blank=True)

    def add_recipe(self, recipe):
        new_entry = Recipe.objects.create(
            name = recipe['name'],
            link = recipe['link'],
            difficulty = recipe['difficulty'],
            cost = recipe['cost'],
            prep_time = recipe['prep_time'],
            cook_time = recipe['cook_time'],
            ingredients = recipe['ingredients'],
            steps = recipe['steps'])

        new_entry.save()

    def scrap(self):
        cache = self.cached_links()
        links = scrap_links(cache)
        for link in links:
            recipe = scrap_recipe(link)
            self.add_recipe(recipe)

    def cached_links(self):
        cached_links = set()
        recipes = Recipe.objects.all()
        [cached_links.add(r.link) for r in recipes]
        return cached_links

