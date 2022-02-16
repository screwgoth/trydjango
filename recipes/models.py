from django.db import models
from django.conf import settings
from django.urls import reverse
from .validators import validate_units_measurement
from .utils import number_str_to_float

class Recipe(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	description = models.TextField(blank=True, null=True)
	directions = models.TextField(blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)

	def get_absolute_url(self):
		return reverse('recipes:detail', kwargs={'id': self.id})


class RecipeIngredient(models.Model):
	recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	descrtipion = models.TextField(blank=True, null=True)
	quantity = models.CharField(max_length=50)
	quantity_as_float = models.FloatField(blank=True, null=True)
	unit = models.CharField(max_length=50, validators=[validate_units_measurement])
	direction = models.TextField(blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)

	def get_absolute_url(self):
		return self.recipe.get_absolute_url()

	# Overriding the save method to convert the quantity to float
	def save(self, *args, **kwargs):
		qty = self.quantity
		qty_as_float, qty_as_float_success = number_str_to_float(qty)
		if qty_as_float_success:
			self.quantity_as_float = qty_as_float
		else:
			self.quantity_as_float = None

		super().save(*args, **kwargs)