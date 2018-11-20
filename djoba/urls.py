from . import views
from django.urls import path, include

urlpatterns = [
	path('', views.index, name='index'),
	path('register/', views.register, name='register'),
	path('logout/', views.user_logout, name='logout'),
	path('jobs/', views.get_jobs, name='jobs'),
	path('job_details/<int:pk>', views.job_details, name='job_details'),
	path('new_job/', views.new_job, name='new_job'),
	path('contacts/', views.get_contacts, name='contacts')
]