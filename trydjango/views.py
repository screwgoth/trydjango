from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Articles
import random

def home_view(request, *args, **kwargs):
	article_id = random.randint(1, 4)
	article_obj = Articles.objects.get(id=article_id)
	article_title = article_obj.title
	article_content = article_obj.content
	#Queryset
	article_queryset = Articles.objects.all()

	#my_list = [12, 234, 44, 565, 454] #A simple list of numbers

	context = {
		"object_list": article_queryset,
		#"my_list": my_list,
		"title": article_title,
		"content": article_content,
		"id": article_obj.id,
	}

	#Django Templates
	#render_to_string(template_name, context=None, request=None, using=None)
	HTTP_RESPONSE = render_to_string("home-view.html", context=context)

	# HTTP_RESPONSE ='''
	# 	<h1>{title} - id ({id})</h1>
	# 	<p>{content}</p>
	# '''.format(**context)
	
	return HttpResponse(HTTP_RESPONSE)
