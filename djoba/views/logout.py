from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import authenticate, login
from django.contrib.auth import logout



def user_logout(request):
	logout(request)
	return redirect('login')