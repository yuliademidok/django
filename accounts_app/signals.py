from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

from accounts_app.models import User, Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile(user=instance, slug=slugify(instance.username))
        profile.save()
