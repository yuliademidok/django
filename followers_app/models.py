from django.db import models

from accounts_app.models import User
from tag_app.models import Tag


class Followers(models.Model):
    follower_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="following",
    )
    following_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        related_name="followers"
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        related_name="followers"
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("follower_user", "following_user"), ("follower_user", "tag"),)
        ordering = ['-created']

