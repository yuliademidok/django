from django.db import models

from accounts_app.models import User


class Subscription(models.Model):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name="subscriptions")
    subscription = models.ForeignKey(
        User, on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="subscribers"
    )

    class Meta:
        unique_together = (("subscriber", "subscription"), )
