from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.
from .forms import CustomUserCreationForm


def register(request):
	if request.method == "POST":
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get("username")
			messages.success(request, f"An account is created for {username}")
			return redirect("login")
		else:
			form = UserCreationForm()
		return render(request, "registration/register.html", {"form": form})


def user_login(request):
	if request.mothod == "POST":
		form = AuthenticationForm(date=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			messages.success(request, f"You are logged in as {user.username}")
			return redirect("home")
		else:
			form = AuthenticationForm()
		return render(request, "registration/login.html", {"form": form})


def user_logout(request):
	logout(request)
	messages.success(request, "You have been logged out successfully")
	return redirect("home")


def index(request):
	return render(request, 'templates/Quiz_/home.html')


def game_start(request):
	response = fet