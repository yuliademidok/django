from django.db import models

from comments_app.models import Comment
from publication_app.models import Post


class Tag(models.Model):
    name = models.CharField(max_length=256, blank=False, unique=True)
    post = models.ManyToManyField(Post, related_name="tags")
    comment = models.ManyToManyField(Comment, related_name="tags")

    def __str__(self):
        return self.name
