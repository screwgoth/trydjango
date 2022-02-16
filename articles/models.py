from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify

# Create your models here.
User = settings.AUTH_USER_MODEL
class Articles (models.Model):
	user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=50, blank=True, null=True)
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	# save() method is called when the object is saved.
	# In our case, also when a Form, derived from ModelForms, is saved.
def save(self, *args, **kwargs):
	# # This operation of slufigy()ing is like a pre_sve signal.
	# if self.slug is None :
	# 	self.slug = slugify(self.title)
	super().save(*args, **kwargs)


def slugify_instance_title(instance, save=False):
	print('Slugify instance title')
	slug = slugify(instance.title)
	qs = Articles.objects.filter(slug=slug).exclude(id=instance.id)
	if qs.exists():
		slug = f'{slug}-{instance.id}'
	instance.slug = slug
	if save:
		instance.save()

def article_pre_save(sender, instance, *args, **kwargs):
	#print('Article pre_save signal')
	# Slugify the title before saving.
	if instance.slug is None :
		#instance.slug = slugify(instance.title)
		slugify_instance_title(instance, save=False)
	#print(sender, instance, args, kwargs)

# This can be replaced by the @reciever decorator
pre_save.connect(article_pre_save, sender=Articles)

def article_post_save(sender, instance, created, *args, **kwargs):
	#print('Article post_save signal')
	#print(args, kwargs)
	if created:
		# instance.slug = "this is my slug"
		#instance.save()
		slugify_instance_title(instance, save=True)

post_save.connect(article_post_save, sender=Articles)