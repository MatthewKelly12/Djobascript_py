from django.contrib import admin

# from __future__ import unicode_literals


from djoba.models import Title, Job, Language, Framework, Contact



admin.site.register(Title)
admin.site.register(Job)
admin.site.register(Language)
admin.site.register(Framework)
admin.site.register(Contact)
