from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class JobBooking(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	tech = models.ForeignKey(User, on_delete=models.CASCADE, related_name="technician")
	note_to_tech = models.TextField()
	date = models.DateField()
	time = models.TimeField()
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	service = models.TextField()
	contact = models.CharField(max_length=13)
	done = models.BooleanField(default=False)
	cancel = models.BooleanField(default=False)
	def __str__(self):
		return self.tech.get_short_name().title()