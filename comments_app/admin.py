from django.contrib import admin

from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "post_id", "user_id")
    readonly_fields = ("id", "post_id", "user_id")
