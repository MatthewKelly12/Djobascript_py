from django import forms
from djoba.models import JobSearch
# from django.contrib.auth.models import User

class JobSearchForm(forms.ModelForm):

	class Meta:
		model = JobSearch
		fields = ['name', 'reason','date_created']
		exclude = ['user']