from django.db import models


class Recipe(models.Model):
    title = models.CharField(
        max_length=150,
        null=False,
        blank=False
    )
    description = models.CharField(
        max_length=2000,
        null=False,
        blank=False
    )
    preparation = models.TextField(
        default=""
    )
    prep_time = models.DurationField()
    cook_time = models.DurationField()
    servings = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return self.title
