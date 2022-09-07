import os

# import sentry_sdk
# from sentry_sdk.integrations.django import DjangoIntegration

from .base import *

DEBUG = False
SECRET_KEY = '5_0y4wktd%k8cmbr#v4*93j6i1uv3jo03@c+!a4rq6r(1j8tz&'  # @todo get a key from here https://miniwebtool.com/django-secret-key-generator/
ALLOWED_HOSTS = ['localhost', '3e6beb0.online-server.cloud', '217.160.171.156']  # @todo add your website url in here
cwd = os.getcwd()
# ~ CACHES = {
    # ~ "default": {
        # ~ "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        # ~ "LOCATION": f"{cwd}/.cache"
    # ~ }
# ~ }


# sentry_sdk.init(
#     dsn="",  # @todo add your Sentry DSN key in here
#     integrations=[DjangoIntegration()],
#
#     # If you wish to associate users to errors (assuming you are using
#     # django.contrib.auth) you may enable sending PII data.
#     send_default_pii=True
# )

try:
    from .local import *
except ImportError:
    pass
