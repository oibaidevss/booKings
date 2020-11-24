from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from .forms import RegisterUserForm
from .models import Handyman, Category
# Create your views here.
def user_home(request):
	# user = get_object_or_404(User, pk=pk)
	context = {
		"title": "User",
		# "instance": user,
	}
	return render(request, "users/user_home.html", context)

def user_profile(request, pk):
	user = get_object_or_404(User, pk=pk)
	context = {
		"title": "User",
		"instance": user,
	}
	return render(request, "users/user_profile.html", context)

def register_user(request):
	if request.method == 'POST':
		form = RegisterUserForm(
			request.POST or None, 
			request.FILES or None,
			)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.is_staff = True
			instance.save()
			return redirect('user:login')
	else:
		form = RegisterUserForm()
	context = {
		"form": form,
		"title": "registration form",
	}
	return render(request, "users/register_user.html", context)
def technician_list(request):
	tech = Handyman.objects.all()
	context = {
		'title': "tech list",
		'tech': tech,
	}
	return render(request, "users/user_home.html", context)
# def user_setting(request, pk):
# 	if request.method == 'POST':
# 		form = UserSettingsForm(
# 			request.POST or None,
# 			request.FILES or None,
# 			)
# 		if form.is_valid():
# 			instance = form.save(commit=False)
# 			instance.
def user_login(request):
	next = request.GET.get('next', '/')
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user=authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(next)
			else:
				HttpResponse("Inactive user")
		else:
			return HttpResponseRedirect(settings.LOGIN_URL)
	return render(request, "users/user_login.html", {"redirect_to": next, "title": "Login"})

def user_logout(request):
	logout(request)
	return HttpResponseRedirect(settings.LOGIN_URL)