from django.shortcuts import render
from djoba.models import JobSearch
from django.contrib.auth.models import User

def job_search(request,pk):
	search = JobSearch.objects.filter(id=pk)
	template = 'djoba/job_search.html'

	return render(request,template,{'search':search})