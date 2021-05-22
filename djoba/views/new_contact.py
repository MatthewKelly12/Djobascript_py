from django.shortcuts import render, redirect
from djoba.models import Contact
from djoba.forms import NewContactForm


def new_contact(request):

	if request.method == 'GET':
		contact_form = NewContactForm()
		template_name = 'djoba/new_contact.html'
		return render(request, template_name, {'contact_form': contact_form})

	elif request.method == 'POST':
		contact_form = NewContactForm(data=request.POST)

		if contact_form.is_valid():
			contact = contact_form.save(commit=False)
			contact.user = request.user
			contact.save()

		url = 'contacts'
		return redirect(url)
