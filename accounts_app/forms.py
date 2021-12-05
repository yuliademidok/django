from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from accounts_app.models import User


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    error_css_class = 'error'
    required_css_class = 'required'
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 }))


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email"]

    error_css_class = 'error'
    required_css_class = 'required'

    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))

