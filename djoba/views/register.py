from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login




def	register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)


		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('index')
	else:
		form = UserCreationForm()
	template = 'registration/register.html'
	context = {'form': form}
	return render(request, template, context)