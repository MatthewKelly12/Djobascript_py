from djoba.models import job_search
from django.db import models
from .language import Language
from .framework import Framework
from .title import Title
from .job_search import JobSearch
from django.contrib.auth.models import User

class Job(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	job_search = models.ForeignKey(JobSearch,on_delete=models.CASCADE)
	company_name = models.CharField(max_length=80)
	title =	models.ForeignKey(Title,on_delete=models.CASCADE)
	date_added = models.DateTimeField(auto_now=False, auto_now_add=False)
	language = models.ManyToManyField(Language)
	framework = models.ManyToManyField(Framework)
	description = models.TextField()

	def __str__(self):
		return self.company_name