import re

from django.db.models.signals import post_save
from django.dispatch import receiver

from comments_app.models import Comment
from publication_app.models import Post
from .models import Tag


# @receiver(post_save, sender=Comment)
@receiver(post_save, sender=Post)
def create_tag(sender, instance, created, **kwargs):
    if created:
        pattern = re.compile(r"#(\w+)")
        tags = pattern.findall(instance.text.lower())
        for tag_name in tags:
            tag, is_created = Tag.objects.get_or_create(name=tag_name)
            tag.post.add(instance)
