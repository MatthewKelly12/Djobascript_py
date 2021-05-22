from django.shortcuts import render
from djoba.models import Contact
from django.contrib.auth.models import User




def get_contacts(request):
	contacts = Contact.objects.filter(user=request.user.id)

	template = 'djoba/contacts.html'

	return render(request, template, {'contacts': contacts})