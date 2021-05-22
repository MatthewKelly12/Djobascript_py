from django import forms
from djoba.models import Contact




class NewContactForm(forms.ModelForm):

	class Meta:
		model = Contact
		fields = ['name','company_name','title','email','phone','date_added','description']
		exclude = ['user']


