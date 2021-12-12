from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms

from accounts_app.models import User, Profile


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")

    username = forms.CharField()


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("avatar", "bio", "phone", "github",)


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", )
        exclude = ("password", )
