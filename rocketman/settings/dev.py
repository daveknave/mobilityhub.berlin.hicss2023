from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-k!zs5how$@a4&hxka-n+)y$tzssu28zin33b6v2s@y^*v382hi'

# SECURITY WARNING: define the correct hosts in production!
# ALLOWED_HOSTS = ['*'] 
ALLOWED_HOSTS = ['localhost', '3e6beb0.online-server.cloud', '217.160.171.156'] 
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
]


try:
    from .local import *
except ImportError:
    pass
