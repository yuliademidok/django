from django.contrib import admin

from tag_app.models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    readonly_fields = ("id", "post", )
