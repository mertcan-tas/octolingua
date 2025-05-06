from django.urls import path
from testing.views import NoAuthTokenView, AutoLoginAdmin
from decouple import config

urlpatterns = [
    path('testing/auth/session/', AutoLoginAdmin, name='testing-auth-session'),
    path('testing/auth/api/', NoAuthTokenView.as_view(), name='testing-auth-api'),
]