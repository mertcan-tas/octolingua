from rest_framework import generics, status, permissions
from rest_framework.response import Response
from authentication.serializers import ChangePasswordSerializer
from decouple import config

from drf_spectacular.utils import extend_schema

SEND_PASSWORD_CHANGE_NOTIFICATION_EMAIL=config("SEND_PASSWORD_CHANGE_NOTIFICATION_EMAIL", default=False, cast=bool)

@extend_schema(tags=['Authentication'], description='Login Auth')
class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = (permissions.IsAuthenticated,)
    http_method_names = ['put'] 
    
    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            if SEND_PASSWORD_CHANGE_NOTIFICATION_EMAIL:
                send_password_change_notification.delay(request.user.email)

            return Response({"message": "Password successfully changed!"}, 
                          status=status.HTTP_200_OK)
                          
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)