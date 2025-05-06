from rest_framework_simplejwt.views import TokenObtainPairView
from authentication.serializers import CustomTokenObtainPairSerializer

from drf_spectacular.utils import extend_schema

@extend_schema(
    tags=['Authentication'],
    description='Login Auth',
)
class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
