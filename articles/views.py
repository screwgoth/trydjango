from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Articles
from .forms import ArticleForm

# login_requried decorator to protect creating Articles by any visitor.
@login_required
def article_create_view(request):
	form = ArticleForm(request.POST or None)
	context = {
		'form': form,
	}
	# is_valid() checks against all the "clean()" methods of the ArticleForm class
	if form.is_valid():
		article_object = form.save() # That's it!!
		# title = form.cleaned_data.get('title')
		# content = form.cleaned_data.get('content')
		# article_object = Articles.objects.create(title=title, content=content)

		# This is also one way to populate context
		context['object'] = article_object
		# Context can have any fields.
		context['created'] = True
		
	return render(request, "articles/create.html", context=context)

# Reference class for creating a view without full use of Forms	
# def article_create_view(request):
# 	#print(request.POST)
# 	form = ArticleForm()
# 	#print(dir(form))
# 	context = {
# 		"form": form,
# 	}
# 	if request.method == 'POST':
# 		form = ArticleForm(request.POST)
# 		# Set the contenxt, so we can show the validation error if the Form is not clean
# 		context['form'] = form
# 		# is_valid() checks against all the "clean()" methods of the ArticleForm class
# 		if form.is_valid():
# 			title = form.cleaned_data.get('title')
# 			content = form.cleaned_data.get('content')
# 			# title = request.POST.get('title')
# 			# content = request.POST.get('content')
# 			#print(title, content)
# 			article_object = Articles.objects.create(title=title, content=content)
# 			# This is also one way to populate context
# 			context['object'] = article_object
# 			# Context can have any fields.
# 			context['created'] = True
		
# 	return render(request, "articles/create.html", context=context)

def article_search_view(request):
	# print(request)
	query_dict = request.GET # this is a dictionary
	try:
		# Convert the query to a number, so we can search against ID.
		query = int(query_dict.get('q')) #<input type='input' name='q'/>
	except:
		query = None
	article_obj = None
	if query is not None:
		article_obj = Articles.objects.get(id=query)
	context = {
		"object": article_obj,
	}
	return render(request, "articles/search.html", context=context)

# For each new argument, add argument to the function
def article_detail_view(request, id=None):
	# print(request)
	article_obj = None
	#Check id is not None
	if id is not None:
		article_obj = Articles.objects.get(id=id)

	context = {
		"object": article_obj,
	}
	# render(request, template, context)
	# This is similar to render_to_string
	return render(request, "articles/detail.html", context=context)