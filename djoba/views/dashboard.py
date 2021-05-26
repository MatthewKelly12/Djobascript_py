from django.shortcuts import render
from djoba.models import JobSearch
from djoba.models import Job

def dashboard(request):
	searches = JobSearch.objects.filter(user=request.user.id).order_by('-date_created')
	template = 'djoba/dashboard.html'

	return render(request,template,{'searches':searches})
