from django.urls import path

from verification.views import (
    SendVerificationEmailView,
    VerifyEmailAPIView
)

urlpatterns = [
    path('send-verification-email/', SendVerificationEmailView.as_view(), name='send_verification_email'),
    path('verify-email/<str:token>/', VerifyEmailAPIView.as_view(), name='verify_email_api'),
]