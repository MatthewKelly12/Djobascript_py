from django.shortcuts import render
from djoba.models import Job
from djoba.models import JobSearch
from django.contrib.auth.models import User

def get_jobs(request):
	jobs = Job.objects.filter(user=request.user.id)
	search_jobs = []
	# searches = JobSearch.objects.filter(id=jobs.job_search_id)
	# for job in jobs:
	# 	if
	# search = JobSearch.objects.filter(id=pk)
	# job_count = Job.objects.filter(job_search_id=pk).count()
	# print(job_count)
	template = 'djoba/jobs.html'

	return render(request, template, {'jobs': jobs})