from django.contrib import admin

from profile_app.models import Profile
from .models import User


class ProfileInLint(admin.StackedInline):
    model = Profile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", )
    inlines = (ProfileInLint, )
