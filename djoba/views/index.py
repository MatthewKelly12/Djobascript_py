from django.shortcuts import render, redirect
from .get_jobs import get_jobs


def index(request):
	template = 'djoba/home.html'
	if request.user.is_authenticated:
		return render(request, template)
	else:
		return redirect('login')