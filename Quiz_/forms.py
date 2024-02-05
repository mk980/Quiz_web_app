from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
	username = forms.CharField(
		max_length=150, widget=forms.TextInput(attrs={"class": "form-control"})
	)
	email = forms.EmailField(
		max_length=254, widget=forms.EmailField(attrs={"class": "form-control"})
	)
	password1 = forms.CharField(
		strip=False, widget=forms.PasswordInput(attrs={"class": "form-control"})
	)
	password2 = forms.CharField(
		strip=False, widget=forms.PasswordInput(attrs={"class": "form-control"})
	)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	class CustomAuthenticationForm(AuthenticationForm):
		username = forms.CharField(
			max_length=254,
			widget=forms.TextInput(attrs={"autofocus": True}),
			error_messages={"required": "Please enter a valid username."},
		)
		password = forms.CharField(
			strip=False,
			widget=forms.PasswordInput,
			error_messages={"required": "Please enter your password."},
		)

		class Meta:
			model = User
			fields = ("username", "password")