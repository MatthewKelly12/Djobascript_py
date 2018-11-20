from django.db import models
# from .language import Language
# from .framework import Framework
# from .title import Title
from django.contrib.auth.models import User

class Contact(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	name = models.CharField(max_length=80)
	email = models.CharField(max_length=150)
	phone = models.CharField(max_length=20)
	company_name = models.CharField(max_length=80)
	title =	models.CharField(max_length=50)
	date_added = models.DateField(auto_now=False, auto_now_add=False)
	description = models.TextField()

	def __str__(self):
		return self.name