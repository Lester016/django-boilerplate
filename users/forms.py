from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email is already registered!")
        return email

    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2"]
