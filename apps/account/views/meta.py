from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from account.models import User
from rest_framework.permissions import AllowAny


class UserMetadataAPIView(APIView):
    permission_classes = [AllowAny]
    
    CACHE_KEY_PREFIX = "user_metadata_"
    CACHE_TIMEOUT = 900
    
    def _get_user_metadata(self, user):
        return {
            "published": user.pets.count(),
            "followers": user.followers.count(),
            "following": user.following.count(),
            "bought": 1,
            "favourites": 3, 
        }
    
    def get(self, request, user_id):
        if not user_id:
            return Response(
                {"error": "User ID is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        cache_key = f"{self.CACHE_KEY_PREFIX}{user_id}"
        cached_data = cache.get(cache_key)
        
        if cached_data is not None:
            return Response({
                "data": {"counters": cached_data},
            })
        
        try:
            user = User.objects.get_object_by_public_id(public_id=user_id)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": f"An error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        metadata = self._get_user_metadata(user)
        cache.set(cache_key, metadata, timeout=self.CACHE_TIMEOUT)

        return Response({
            "data": {"counters": metadata},
        })