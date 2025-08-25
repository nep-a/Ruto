from django.contrib import admin
from .models import Service, Appointment, Testimonial, ContactMessage


class AppointmentInline(admin.TabularInline):
	model = Appointment
	extra = 0
	fields = ('customer_name', 'car_model', 'phone', 'preferred_datetime', 'status')
	show_change_link = True


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
	list_display = ('name', 'price')
	search_fields = ('name',)
	inlines = [AppointmentInline]


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
	list_display = (
		'customer_name', 'phone', 'car_model', 'service', 'preferred_datetime', 'status', 'created_at'
	)
	list_filter = ('status', 'preferred_datetime', 'created_at')
	search_fields = ('customer_name', 'phone', 'car_model')
	list_editable = ('status',)
	date_hierarchy = 'preferred_datetime'
	ordering = ('-preferred_datetime',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
	list_display = ('customer_name', 'rating', 'created_at')
	list_filter = ('rating', 'created_at')
	search_fields = ('customer_name', 'message')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'date')
	list_filter = ('date',)
	search_fields = ('name', 'email', 'message')
