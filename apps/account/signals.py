from django.db.models.signals import post_save
from django.dispatch import receiver
from versatileimagefield.image_warmer import VersatileImageFieldWarmer

from account.models import User, Profile

@receiver(post_save, sender=User)
def create_user_related_models(sender, instance, created, **kwargs):
    if created:
        name = getattr(instance, '_name', '')
        surname = getattr(instance, '_surname', '')
        
        Profile.objects.create(user=instance, name=name, surname=surname)


@receiver(post_save, sender=Profile)
def warm_avatar_image(sender, instance, **kwargs):
    if instance.avatar and hasattr(instance.avatar, 'name') and instance.avatar.name:
        profile_img_warmer = VersatileImageFieldWarmer(
            instance_or_queryset=instance,
            rendition_key_set='avatar',
            image_attr='avatar'  
        )
        num_created, failed_to_create = profile_img_warmer.warm()
        if failed_to_create:
            print(f"Failed to create {failed_to_create} image renditions for Profile {instance.id}")