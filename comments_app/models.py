from django.db import models

from accounts_app.models import User
from publication_app.models import Post


class Comment(models.Model):
    text = models.TextField(null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False, related_name="comments")


