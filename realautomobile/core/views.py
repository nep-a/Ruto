from django.contrib import messages
from django.core.mail import mail_admins
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Service, Testimonial
from .forms import AppointmentForm, ContactForm


def home(request):
	services = Service.objects.all()[:6]
	testimonials = Testimonial.objects.order_by('-created_at')[:5]
	return render(request, 'core/home.html', {'services': services, 'testimonials': testimonials})


def services(request):
	services_qs = Service.objects.all()
	return render(request, 'core/services.html', {'services': services_qs})


def book_appointment(request):
	if request.method == 'POST':
		form = AppointmentForm(request.POST)
		if form.is_valid():
			appointment = form.save()
			messages.success(request, 'Your appointment request has been submitted! We will contact you to confirm.')
			# Optional: notify admins
			mail_admins(
				subject='New Appointment Request',
				message=f"Appointment by {appointment.customer_name} for {appointment.service.name} on {appointment.preferred_datetime}",
				fail_silently=True,
			)
			return redirect(reverse('home'))
	else:
		form = AppointmentForm()
	return render(request, 'core/book_appointment.html', {'form': form})


def about(request):
	return render(request, 'core/about.html')


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
			return redirect(reverse('contact'))
	else:
		form = ContactForm()
	return render(request, 'core/contact.html', {'form': form})
