from django.contrib import admin

from .models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("id", "post_id", "user_id")
    readonly_fields = ("id", "post_id", "user_id")
