from .settings import *
import os

# Production settings
DEBUG = False

ALLOWED_HOSTS = [
    'fallout-room-backend.onrender.com',
    'localhost',
    '127.0.0.1',
]

# Database for production (Render auto-configures this)
import dj_database_url
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# CORS for your frontend
CORS_ALLOWED_ORIGINS = [
    "https://harjin2005.github.io",
]

# Security settings
SECURE_SSL_REDIRECT = False  # Render handles SSL
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
