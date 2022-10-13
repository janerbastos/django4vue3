from django.dispatch import receiver
from django.db.models.signals import (pre_save, post_save)

# Model
from .models import (User, UserProfile)

@receiver(post_save, sender=User)
def post_save_profile_receiver(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        try:
            user = UserProfile.objects.get(user=instance)
        except:
            # Create profile is not exists
            UserProfile.objects.create(user=instance)


@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwards):
    pass