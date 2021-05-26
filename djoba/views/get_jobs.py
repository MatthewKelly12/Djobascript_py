from django.shortcuts import render
from djoba.models import Job
from django.contrib.auth.models import User

def get_jobs(request):
	jobs = Job.objects.filter(user=request.user.id)
	template = 'djoba/jobs.html'

	return render(request, template, {'jobs': jobs})