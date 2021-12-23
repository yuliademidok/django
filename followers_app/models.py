from django.db import models

from accounts_app.models import User


class Followers(models.Model):
    follower_user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name="following")
    following_user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="followers"
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("follower_user", "following_user"), )
        ordering = ['-created']

