from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	address = models.CharField(max_length=200)
	# contact_number = models.IntegerField()
	def __str__(self):
		return self.user.get_username().upper()