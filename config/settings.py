from pathlib import Path
from decouple import config, Csv
from datetime import timedelta
import sys
import os

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, os.path.join(BASE_DIR, 'apps')) 

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    'storages',
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'django_celery_results',
    'drf_spectacular',
    'django_prometheus',
    'versatileimagefield',
]

PROJECT_APPS = [
    'core',
    'account',
    'verification',
    'api',
]

PROJECT_APPS.append('testing') if config("DEBUG", default=False, cast=bool) else None

INSTALLED_APPS += PROJECT_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

AUTH_USER_MODEL = 'account.User'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("POSTGRES_DB"),
        "USER": config("POSTGRES_USER"),
        "PASSWORD": config("POSTGRES_PASSWORD"),
        "HOST": config("POSTGRES_HOST"),
        "PORT": config("POSTGRES_PORT"),
    },
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f'redis://:{config('REDIS_PASSWORD')}@{config('REDIS_HOST')}/{config('REDIS_DB')}',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {
                "max_connections": 200,
            },
            "SOCKET_TIMEOUT": 1.5,
            "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
            "COMPRESS_LEVEL": 4,
            "COMPRESS_MIN_LENGTH": 1024,
            "SERIALIZER": "django_redis.serializers.msgpack.MSGPackSerializer",
            "HEALTH_CHECK_INTERVAL": 30,
            "PERSISTENT": True,
        },
        "KEY_PREFIX": "pawiscor",
        "VERSION": 1
    }
}

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [f'redis://:{config('REDIS_PASSWORD')}@{config('REDIS_HOST')}/{config('REDIS_DB')}'],
        },
    },
}

CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_BROKER_URL = f'redis://:{config('REDIS_PASSWORD')}@{config('REDIS_HOST')}/{config('REDIS_DB')}'
CELERY_TIMEZONE = 'Europe/Istanbul'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"



EMAIL_BACKEND = config('EMAIL_BACKEND', default="django.core.mail.backends.smtp.EmailBackend", cast=str)
EMAIL_HOST = config('EMAIL_HOST', default="localhost", cast=str)   
EMAIL_PORT = config('EMAIL_PORT', default=1025, cast=int)             
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False, cast=bool)       
EMAIL_USE_SSL = config('EMAIL_USE_SSL', default=False, cast=bool)        
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default="noreply@app.com", cast=str)           
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default="", cast=str)


MINIO_ENDPOINT = config('MINIO_ENDPOINT', default='localhost:9000', cast=str)
MINIO_ACCESS_KEY = config('MINIO_ACCESS_KEY', default='minioadmin', cast=str)
MINIO_SECRET_KEY = config('MINIO_SECRET_KEY', default='minioadmin', cast=str)
MINIO_USE_HTTPS = config('MINIO_USE_HTTPS', default=False, cast=bool)
MINIO_BUCKET_NAME = config('MINIO_BUCKET_NAME', default='files', cast=str)

AWS_S3_ENDPOINT_URL = f'http://{MINIO_ENDPOINT}'
AWS_ACCESS_KEY_ID = MINIO_ACCESS_KEY
AWS_SECRET_ACCESS_KEY = MINIO_SECRET_KEY
AWS_STORAGE_BUCKET_NAME = MINIO_BUCKET_NAME
AWS_S3_USE_SSL = MINIO_USE_HTTPS
AWS_S3_FILE_OVERWRITE = False
AWS_QUERYSTRING_AUTH = False
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

AWS_LOCATION = 'media'
AWS_STATIC_LOCATION = 'static'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STORAGES = {
    "default": {
        "BACKEND": DEFAULT_FILE_STORAGE,
        "OPTIONS": {
            "location": AWS_LOCATION,
        },
    },
    "staticfiles": {
        "BACKEND": STATICFILES_STORAGE,
        "OPTIONS": {
            "location": AWS_STATIC_LOCATION,
        },
    }
}

VERSATILEIMAGEFIELD_SETTINGS = {
    'cache_length': 2592000,
    'cache_name': 'versatileimagefield_cache',
    'jpeg_resize_quality': 85,
    'sized_directory_name': '__sized__',
    'filtered_directory_name': '__filtered__',
    'placeholder_directory_name': '__placeholder__',
    'create_images_on_demand': True,
    'image_key_post_processor': None,
    'progressive_jpeg': False,
}

VERSATILEIMAGEFIELD_RENDITION_KEY_SETS = {
    'avatar': [
        ('full_size', 'url'),
        ('square_crop', 'crop__300x300'),
        ('thumbnail', 'thumbnail__600x600'),
    ],
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=10),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
    'SLIDING_TOKEN_LIFETIME': timedelta(days=30),
    'SLIDING_TOKEN_REFRESH_LIFETIME_LATE_USER': timedelta(days=1),
    'SLIDING_TOKEN_LIFETIME_LATE_USER': timedelta(days=30),
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Pawhub',
    'DESCRIPTION': 'Pawhub helps cat & dog owners find suitable matches for breeding. Create profiles, explore matches by location and traits, and connect easily—all in one safe platform.',
    'VERSION': '1.0.1',
    'SERVE_INCLUDE_SCHEMA': False,
}


CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    "http://127.0.0.1:5173",
    "http://localhost:5173", 
]

CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    "http://127.0.0.1:5173",
    "http://localhost:5173", 
]

CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = ['http://localhost']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'http')
CSRF_COOKIE_HTTPONLY = False

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
