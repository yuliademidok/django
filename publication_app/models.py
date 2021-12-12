from django.conf import settings
from django.db import models
from django.urls import reverse


class Post(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    title = models.CharField(max_length=256, unique=False, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    image = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="posts"
    )

    def get_absolute_url(self):
        return reverse("publication:post_result", kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-create_date']
