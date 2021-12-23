from django.contrib import admin

from .models import Followers


@admin.register(Followers)
class FollowersAdmin(admin.ModelAdmin):
    list_display = ("id", "follower_user", "following_user")
