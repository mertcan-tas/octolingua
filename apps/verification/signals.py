from django.db.models.signals import post_save
from django.dispatch import receiver

from account.models import User
from verification.models import AccountVerification

@receiver(post_save, sender=User)
def create_user_related_models(sender, instance, created, **kwargs):
    if created:        
        AccountVerification.objects.create(user=instance)