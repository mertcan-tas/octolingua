from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from authentication.serializers import RegisterSerializer
from decouple import config
from drf_spectacular.utils import extend_schema

User = get_user_model()

SEND_WELCOME_EMAIL=config("SEND_WELCOME_EMAIL", default=False, cast=bool)

@extend_schema(tags=['Authentication'], description='Register Auth')
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
    
    def perform_create(self, serializer):
        if SEND_WELCOME_EMAIL:
            send_welcome_email.delay(user.email)
        user = serializer.save()
