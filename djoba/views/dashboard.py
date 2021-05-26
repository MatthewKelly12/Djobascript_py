from django.shortcuts import render
from djoba.models import JobSearch
from djoba.models import Job

def dashboard(request):
	searches = JobSearch.objects.filter(user=request.user.id)
	print(searches)
	template = 'djoba/dashboard.html'
	return render(request,template,{'searches':searches})

	# jobs = Job.objects.filter(user=request.user.id)
	# template = 'djoba/jobs.html'

	# return render(request, template, {'jobs': jobs})