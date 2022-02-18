from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_list_or_404, redirect
from .models import Recipe
from .forms import RecipeForm

# Create your views here.
@login_required
def recipe_list_view(request):
	qs = Recipe.objects.filter(user=request.user)
	context = {
		"object_list": qs
	}
	return render(request, 'recipes/list.html', context=context)

@login_required
def recipe_detail_view(request, id=None):
	obj = get_list_or_404(Recipe, id=id, user=request.user)
	context = {
		"object": obj
	}

	return render(request, 'recipes/detail.html', context=context)

@login_required
def recipe_create_view(request):
	form = RecipeForm(request.POST or None)
	context = {
		"form": form
	}
	if form.is_valid():
		obj = form.save(commit=False)
		# Rememeber Form will be filled without information of which user filled it.
		# So we manually updated the user, since we know user is logged in.
		obj.user = request.user
		obj.save()
		return redirect(obj.get_absolute_url())
	return render(request, 'recipes/create-update.html', context=context)

@login_required
def recipe_update_view(request, id=None):
	obj = get_list_or_404(Recipe, id=id, user=request.user)
	form = RecipeForm(request.POST or None, instance=obj)
	context = {
		"form": form,
		"object": obj
	}
	if form.is_valid():
		form.save()
		context['message'] = "Recipe Updated"
	return render(request, 'recipes/create-update.html', context=context)