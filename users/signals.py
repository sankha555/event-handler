from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Creator

@receiver(pre_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Creator.objects.create(user=instance)

@receiver(pre_save, sender=User)
def save_profile(sender, instance, **kwargs):
        instance.creator.save()
