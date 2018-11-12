from django.shortcuts import render, redirect




def index(request):
	template = 'djoba/home.html'
	if request.user.is_authenticated:

		return render(request, template)
	else:
		return redirect('login')