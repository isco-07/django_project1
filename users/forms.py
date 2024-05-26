from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from catalog.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class LoginUserForm(StyleFormMixin, AuthenticationForm):
    class Meta:
        model = User
        fields = ("email", "password")


class PasswordResetForm(StyleFormMixin, forms.Form):
    email = forms.EmailField(label="email")
