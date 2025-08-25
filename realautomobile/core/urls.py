from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('services/', views.services, name='services'),
	path('book-appointment/', views.book_appointment, name='book_appointment'),
	path('about/', views.about, name='about'),
	path('contact/', views.contact, name='contact'),
]