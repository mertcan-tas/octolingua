from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer
from django.conf import settings

from account.models import Profile

class ProfileSerializer(serializers.ModelSerializer):   
    avatar = VersatileImageFieldSerializer(
        sizes=settings.VERSATILEIMAGEFIELD_RENDITION_KEY_SETS['avatar']
    )
    
    class Meta:
        model = Profile
        fields = ('full_name', 'about', 'avatar', 'created_at')

class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'surname', 'about')
        extra_kwargs = {
            "name": {"required": True},
            "surname": {"required": True},
        }