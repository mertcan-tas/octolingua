# account/views/verification_views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from account.models import User
from account.serializers import VerificationStatusSerializer


class VerificationStatusView(APIView):
    CACHE_KEY_PREFIX = "verification_status_"
    CACHE_TIMEOUT = 900
    
    def get(self, request, user_id):
        cache_key = f"{self.CACHE_KEY_PREFIX}{user_id}"
        cached_data = cache.get(cache_key)
        
        if cached_data is not None:
            return Response({
                "data": {"status": cached_data},
            })
        
        try:
            user = User.objects.get_object_by_public_id(public_id=user_id)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        verification_status = VerificationStatusSerializer.get_verification_status_for_user(user)
        cache.set(cache_key, verification_status, timeout=self.CACHE_TIMEOUT)

        return Response({
            "data": {"status": verification_status},
        })