import uuid

from django.db import models

from django.conf import settings


class Ingredient(models.Model):
    """Ingredient to be used in a recipe"""
    name = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Recipe object"""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=1000, null=False, blank=False)
    ingredients = models.ManyToManyField('Ingredient')
    instructions = models.TextField()
    preparation_time = models.DurationField()
    cooking_time = models.DurationField()
    image = models.ImageField(null=True, upload_to='recipe_image')

    def __str__(self):
        return self.title