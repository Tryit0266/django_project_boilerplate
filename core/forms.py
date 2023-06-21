from django import forms
from allauth.account.forms import LoginForm, SignupForm


class CustomLoginForm(LoginForm):
    login = forms.CharField(required=True, max_length=20)
    password = forms.CharField(required=True, max_length=20)


class CustomSignupForm(SignupForm):
    username = forms.CharField(required=True, max_length=20)
    email = forms.CharField(required=True, max_length=20)
    password1 = forms.CharField(required=True, max_length=20)
    password2 = forms.CharField(required=True, max_length=20)
