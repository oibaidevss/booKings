from django.urls import path
from . import views

APP_NAME = "user"
urlpatterns = [
	path('', views.user_home, name="home"),
	path('<int:pk>', views.user_profile, name="profile"),
	path('register/', views.register_user, name="register"),
	path('login/', views.user_login, name="login"),
	path('logout/', views.user_logout, name="logout"),
	path('tech/', views.technician_list, name="list"),
]