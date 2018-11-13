from . import views
from django.urls import path, include

urlpatterns = [
	path('', views.index, name='index'),
	path('register/', views.register, name='register'),
	path('logout/', views.user_logout, name='logout'),
	path('jobs/', views.get_jobs, name='jobs')
]