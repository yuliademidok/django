from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator

from accounts_app.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=False, related_name="profile")
    avatar = models.ImageField(default='default.png', upload_to='profile_images')
    phone = models.CharField(
        max_length=16,
        validators=(
            RegexValidator(regex=r"^\+?\d{8, 15}$", message="Invalid phone number"),
        ),
        blank=True,
        null=True,
    )
    bio = models.TextField(null=True, blank=True)
    github = models.URLField(max_length=2048, null=True, blank=True)

    slug = models.SlugField(null=False, blank=False, unique=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("profile:profile", kwargs={'slug': self.slug})

    @property
    def username(self):
        return self.user.username
