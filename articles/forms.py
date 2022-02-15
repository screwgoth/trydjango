from django import forms

class ArticleForm(forms.Form):
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

		