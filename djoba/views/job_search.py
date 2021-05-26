from django.shortcuts import render

def job_search(request):
	template = 'djoba/job_search.html'
	return render(request,template)