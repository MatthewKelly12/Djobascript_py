from django.shortcuts import render
from djoba.models import Job
from djoba.models import JobSearch
from django.contrib.auth.models import User

def get_jobs(request,pk):
	jobs = Job.objects.filter(user=request.user.id).filter(job_search_id=pk)
	template = 'djoba/jobs.html'

	return render(request, template, {'jobs': jobs})