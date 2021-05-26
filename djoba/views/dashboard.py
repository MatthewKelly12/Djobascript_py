from django.shortcuts import render

def dashboard(request):
	template = 'djoba/dashboard.html'
	return render(request,template)