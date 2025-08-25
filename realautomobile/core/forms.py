from django import forms
from django.utils import timezone

from .models import Appointment, ContactMessage


class AppointmentForm(forms.ModelForm):
	preferred_datetime = forms.DateTimeField(
		widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
		input_formats=['%Y-%m-%dT%H:%M']
	)

	class Meta:
		model = Appointment
		fields = ['customer_name', 'phone', 'car_model', 'service', 'preferred_datetime']
		widgets = {
			'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
			'phone': forms.TextInput(attrs={'class': 'form-control'}),
			'car_model': forms.TextInput(attrs={'class': 'form-control'}),
			'service': forms.Select(attrs={'class': 'form-select'}),
		}

	def clean_preferred_datetime(self):
		value = self.cleaned_data['preferred_datetime']
		if value < timezone.now():
			raise forms.ValidationError('Preferred date and time cannot be in the past.')
		return value


class ContactForm(forms.ModelForm):
	class Meta:
		model = ContactMessage
		fields = ['name', 'email', 'message']
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.EmailInput(attrs={'class': 'form-control'}),
			'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
		}
