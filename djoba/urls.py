from . import views
from django.urls import path, include

urlpatterns = [
	path('', views.index, name='index'),
	path('register/', views.register, name='register'),
	path('logout/', views.user_logout, name='logout'),
	path('jobs/', views.get_jobs, name='jobs'),
	path('job_details/<int:pk>', views.job_details, name='job_details'),
	path('new_job/', views.new_job, name='new_job'),
	path('contacts/', views.get_contacts, name='contacts'),
	path('contact_details/<int:pk>', views.contact_details, name='contact_details'),
	path('new_contact/', views.new_contact, name='new_contact'),
	path('job_search/', views.job_search,name='job_search'),
]