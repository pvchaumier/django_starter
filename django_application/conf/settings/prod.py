"""Production settings."""

from .base import *


################
#
# SECURITY
#
################
# SECURITY and DEPLOYMENT SPECIFICS
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
DEBUG = False
ALLOWED_HOSTS = ['YOUR-ALLOWED-HOSTS']
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = False
SESSION_COOKIE_SECURE = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
X_FRAME_OPTIONS = 'DENY'
