from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.category_name
    class Meta:
        verbose_name_plural = 'categories'
class Handyman(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, through="TechMembership")
    def __str__(self):
        return self.category.category_name
    class Meta:
        verbose_name_plural = 'handymen'
class TechMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    handyman = models.ForeignKey(Handyman, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.handyman.category.category_name
    class Meta:
        verbose_name_plural = 'technician memberships'