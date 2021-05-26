from django.db import models
from .language import Language
from .framework import Framework
from .title import Title
from django.contrib.auth.models import User

class JobSearch(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	name =	models.CharField(max_length=150)
	reason = models.TextField()
	date_created = models.DateField(auto_now=False, auto_now_add=False)
	date_ended = models.DateField(auto_now=False, auto_now_add=False, null=True)
	date_modified = models.DateField(auto_now=False, auto_now_add=False)

	def __str__(self):
		return self.name