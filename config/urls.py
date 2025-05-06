from django.contrib import admin
from django.urls import path,re_path, include
from decouple import config
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('account.urls')),
    path('api/auth/', include('authentication.urls')),
    path('api/verification/', include('verification.urls')),
    path('api/v1/', include('api.urls')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),    
]

urlpatterns.append(path('', include('testing.urls'))) if config("DEBUG", default=False, cast=bool) else None


