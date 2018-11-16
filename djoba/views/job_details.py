from django.shortcuts import render
from djoba.models import Job
from django.contrib.auth.models import User




def job_details(request, pk):
	job = Job.objects.filter(id=pk)

	template = 'djoba/job_details.html'

	return render(request, template, {'job': job})