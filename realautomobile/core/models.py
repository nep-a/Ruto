from django.db import models


class Service(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	price = models.DecimalField(max_digits=8, decimal_places=2)

	def __str__(self) -> str:
		return self.name


class Appointment(models.Model):
	STATUS_PENDING = 'pending'
	STATUS_CONFIRMED = 'confirmed'
	STATUS_COMPLETED = 'completed'
	STATUS_CHOICES = [
		(STATUS_PENDING, 'Pending'),
		(STATUS_CONFIRMED, 'Confirmed'),
		(STATUS_COMPLETED, 'Completed'),
	]

	customer_name = models.CharField(max_length=100)
	phone = models.CharField(max_length=20)
	car_model = models.CharField(max_length=100)
	service = models.ForeignKey(Service, on_delete=models.PROTECT, related_name='appointments')
	preferred_datetime = models.DateTimeField()
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_PENDING)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self) -> str:
		return f"{self.customer_name} - {self.preferred_datetime:%Y-%m-%d %H:%M}"


class Testimonial(models.Model):
	customer_name = models.CharField(max_length=100)
	message = models.TextField()
	rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self) -> str:
		return f"{self.customer_name} ({self.rating}/5)"


class ContactMessage(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	message = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self) -> str:
		return f"Message from {self.name}"
