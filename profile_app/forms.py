from django import forms
from django.contrib.auth.forms import UserChangeForm

from accounts_app.models import User
from profile_app.models import Profile


class UpdateProfileForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = ("avatar", "bio", "phone", "github",)


class UpdateUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email",)
