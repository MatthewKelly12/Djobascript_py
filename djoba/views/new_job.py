from django.shortcuts import render, redirect
from djoba.models import Job
from djoba.forms import NewJobForm


def new_job(request):

	if request.method == 'GET':
		job_form = NewJobForm()
		template_name = 'djoba/new_job.html'
		return render(request, template_name, {'job_form': job_form})

	elif request.method == 'POST':
		job_form = NewJobForm(data=request.POST)

		if job_form.is_valid():
			job = job_form.save(commit=False)
			job.user = request.user
			job.save()
		else:
			print('Did Not Save')

		url = 'jobs'
		return redirect(url)
