from .settings import *
import os

# Production settings
DEBUG = False

# Render deployment configuration
ALLOWED_HOSTS = [
    'fallout-room-backend.onrender.com',
    'localhost',
    '127.0.0.1',
    '0.0.0.0',  # Required for Render
]

# Database connection pooling for stability
DATABASES['default']['CONN_MAX_AGE'] = 60

# Database for production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': os.environ.get('DATABASE_PORT'),
    }
}

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# CORS for your frontend
CORS_ALLOWED_ORIGINS = [
    "https://your-username.github.io",  # Replace with your GitHub Pages URL
]

# Security
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
