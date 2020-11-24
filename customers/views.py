from django.shortcuts import render
from .models import Customer
# Create your views here.
def customer_profile(request):
	customer = Customer.objects.all()
	print(request.id)