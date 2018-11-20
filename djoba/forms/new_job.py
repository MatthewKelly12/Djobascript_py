from django import forms
from djoba.models import Job
from django.contrib.auth.models import User



class NewJobForm(forms.ModelForm):

	class Meta:
		model = Job
		fields = ['company_name','title', 'date_added','language','framework','description']
		exclude = ['user']