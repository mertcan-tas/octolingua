from rest_framework import status
from rest_framework.permissions import AllowAny 
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from decouple import config
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from authentication.tasks import send_password_reset_email
from django.utils.decorators import method_decorator
from django_ratelimit.decorators import ratelimit
    
from account.models import User

FRONTEND_URL = config("FRONTEND_URL", default="http://localhost:3000", cast=str)

class PasswordResetRequestView(APIView):
    permission_classes = [AllowAny]
    
    @method_decorator(ratelimit(key='user', rate='5/h', method='POST'))
    def post(self, request):
        email = request.data.get('email')
        if email:
            user = User.objects.filter(email=email).first()
            if user:
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                reset_url = f"{FRONTEND_URL}/reset-password/{uid}/{token}"
                full_name = user.profile.full_name
                send_password_reset_email.delay(email, reset_url, full_name)
                
                return Response({"message": "Password reset email has been sent."}, 
                              status=status.HTTP_200_OK)
            return Response({"message": "User with this email does not exist."}, 
                          status=status.HTTP_404_NOT_FOUND)
        return Response({"email": ["This field is required."]}, 
                       status=status.HTTP_400_BAD_REQUEST)