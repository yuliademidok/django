from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

from accounts_app.models import User
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        slug = slugify(instance.username)
        Profile.objects.create(user=instance, slug=slug)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.slug = slugify(instance.username)
    instance.profile.save()

