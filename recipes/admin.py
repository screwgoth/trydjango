from django.contrib.auth import get_user_model
from django.contrib import admin
from .models import Recipe, RecipeIngredient

# EVERYWHERE other than in the Models, where it is fetched from settings.USER_AUTH_MODEL,
# We get User with get_user_model()
User = get_user_model()
# Not recommeded to unregister User, but this shows
# it can be done
admin.site.unregister(User)

admin.site.register(RecipeIngredient)

class RecipeInline(admin.StackedInline):
	model = Recipe
	extra = 0

class UserAdmin(admin.ModelAdmin):
	inlines = [RecipeInline]
	list_display = ['username']

# Even though User is already registered, we are re-registering it since we made
# changes to UserAdmin. 
# In order to register, we need to unregister above first.
admin.site.register(User, UserAdmin)
# To see the RecipeIngredient model in the admin panel
# class RecipeIngredientInline(admin.TabularInline):
class RecipeIngredientInline(admin.StackedInline):
	model = RecipeIngredient
	fields = ['name', 'quantity', 'unit', 'direction']
	extra = 0 # Otherwise 3 Rows are shown by default
class RecipeAdmin(admin.ModelAdmin):
	# To see the RecipeIngredient model in the admin panel
	inlines = [RecipeIngredientInline]
	list_display = ['name', 'user']
	# readonly_fields = ['timestamp', 'updated']
	# Helps tp add users with ID, which can be used to do lookups in Django Admin
	raw_id_field = ['user']


admin.site.register(Recipe, RecipeAdmin)