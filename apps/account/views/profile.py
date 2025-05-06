from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from account.serializers import ProfileUpdateSerializer, UserSerializer
from account.models import User

class CurrentUserProfileView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user

class UserProfileView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
    def get_object(self):
        user_id = self.kwargs.get('user_id')
        try:
            return User.objects.get_object_by_public_id(public_id=user_id)
        except User.DoesNotExist:
            self.permission_denied(
                self.request,
                message="User not found"
            )

class ProfileUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def put(self, request):
        serializer = ProfileUpdateSerializer(request.user.profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



