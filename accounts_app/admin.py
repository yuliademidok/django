from django.contrib import admin

from .models import User


@admin.register(User)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "username", )

