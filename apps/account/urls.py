from django.urls import path

from account.views import (
    CurrentUserProfileView,
    UserProfileView,
    UserMetadataAPIView,
    ProfileUpdateAPIView,
    VerificationStatusView,
)

urlpatterns = [
    path('user/current/profile/', CurrentUserProfileView.as_view(), name='current-profile'),
    path('user/<uuid:user_id>/profile/', UserProfileView.as_view(), name='user-profile'),
    path('user/profile-update/', ProfileUpdateAPIView.as_view(), name='profile-update'),
    path('user/<uuid:user_id>/metadata/', UserMetadataAPIView.as_view(), name='user-metadata'),
    path('user/<uuid:user_id>/status/', VerificationStatusView.as_view(), name='user-status'),
]