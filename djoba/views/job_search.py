from django.shortcuts import render
from djoba.models import JobSearch
from djoba.models import Job
from django.contrib.auth.models import User

def job_search(request,pk):
	search = JobSearch.objects.filter(id=pk)
	job_count = Job.objects.filter(job_search_id=pk).count()
	print(job_count)
	template = 'djoba/job_search.html'

	return render(request,template,{'search':search,'job_count':job_count})