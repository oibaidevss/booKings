from django.urls import path
from . import views

APP_NAME = "job"
urlpatterns = [
    path('book/', views.job_list, name="list"),
    path('book/add/', views.add_booking, name="add"),
]