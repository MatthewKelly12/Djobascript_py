from django.shortcuts import render

def current_search(request):
	template = 'djoba/current_job_search.html'
	return render(request,template)