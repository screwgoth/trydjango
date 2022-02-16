from django.db import models
from django.conf import settings

class Recipe(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	description = models.TextField(blank=True, null=True)
	directions = models.TextField(blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)


class RecipeIngredient(models.Model):
	recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	descrtipion = models.TextField(blank=True, null=True)
	quantity = models.CharField(max_length=50)
	unit = models.CharField(max_length=50)
	direction = models.TextField(blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)