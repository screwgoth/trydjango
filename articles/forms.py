from django import forms
from .models import Articles

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Articles
		# Always good to declare the fields
		fields = ['title', 'content']
	
	def clean(self):
		data = self.cleaned_data
		title = data.get('title')
		print(title)
		# Queryset to filter data
		qs = Articles.objects.all().filter(title__icontains=title)
		if qs.exists():
			#print(dir(qs))
			# add_error() is another way to inject error. Replaced ValidatioError.
			self.add_error('title', "Title already exists")
		return data

class ArticleFormOld(forms.Form):
	title = forms.CharField()
	content = forms.CharField()

	# Methods to clean data, clean_fieldname
	# def clean_title(self):
	# 	# self.cleaned_data is existing property
	# 	cleaned_data = self.cleaned_data #dictionary
	# 	print('cleaned_data: ', cleaned_data)
	# 	title = cleaned_data.get('title')
	# 	print('title: ', title)
	# 	if title.lower().strip() == 'ugly title':
	# 		raise forms.ValidationError('Title cannot be "ugly title"')
	# 	return title

	# Clean all the fields
	def clean(self):
		cleaned_data = self.cleaned_data
		print('All cleaned_data: ', cleaned_data)
		title = cleaned_data.get('title')
		print('title: ', title)
		if title.lower().strip() == 'ugly title':
			raise forms.ValidationError('Title cannot be "ugly title"')
		return cleaned_data

		