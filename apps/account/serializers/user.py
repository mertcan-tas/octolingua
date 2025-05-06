from rest_framework import serializers
from account.serializers import ProfileSerializer

from account.models import User

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    class Meta:
        model = User
        fields = ('public_id','email', 'profile')