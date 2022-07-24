from django.contrib import admin

from .models import User, Profile


class ProfileInLine(admin.StackedInline):
    model = Profile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", )
    inlines = (ProfileInLine, )
