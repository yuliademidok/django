from django.db import models
from django.urls import reverse

from accounts_app.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.png', upload_to='profile_images')

    slug = models.SlugField(null=False, blank=False, unique=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("profile:profile", kwargs={'slug': self.slug})

    @property
    def username(self):
        return self.user.username
