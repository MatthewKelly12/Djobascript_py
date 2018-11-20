from django.shortcuts import render
# from djoba.models import Job
from django.contrib.auth.models import User




def get_contacts(request):
	# contacts = Job.objects.filter(user=request.user.id)

	template = 'djoba/contacts.html'
	# {'contacts': contacts}
	return render(request, template)