from django.db import models
from .language import Language
from .framework import Framework
from .title import Title

class Job(models.Model):
	company_name = models.CharField(max_length=80)
	title =	models.ForeignKey(Title,on_delete=models.CASCADE)
	date_added = models.DateTimeField(auto_now=False, auto_now_add=False)
	language = models.ManyToManyField(Language)
	framework = models.ManyToManyField(Framework)
	description = models.TextField()

	def __str__(self):
		return self.company_name