from django.shortcuts import render
from djoba.models import Contact


def contact_details(request, pk):
	contact = Contact.objects.filter(id=pk)

	template = 'djoba/contact_details.html'

	return render(request, template, {'contact': contact})