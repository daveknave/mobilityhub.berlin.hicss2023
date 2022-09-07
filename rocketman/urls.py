from django.conf import settings

import pkg_resources

dj_version = pkg_resources.get_distribution("django").version
is_django_4 =  int(dj_version.split('.')[0]) >= 4

if is_django_4:
    from django.urls import include, re_path
else:
    from django.conf.urls import include, url

from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.contrib.sitemaps.views import sitemap
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls



from django.urls import path
from pandasdata import views


if is_django_4:
    urlpatterns = [
        re_path(r'^admin/', include(wagtailadmin_urls)),
        re_path(r'^documents/', include(wagtaildocs_urls)),

        re_path(r'^sitemap.xml$', sitemap),

        re_path(r"pandas", views.Table, name ="table"),

        re_path(r'^accounts/', include('allauth.urls')),

        # For anything not caught by a more specific rule above, hand over to
        # Wagtail's page serving mechanism. This should be the last pattern in
        # the list:
        re_path(r'', include(wagtail_urls)),

        # Alternatively, if you want Wagtail pages to be served from a subpath
        # of your site, rather than the site root:
        #    url(r'^pages/', include(wagtail_urls)),

    ]
else:

    urlpatterns = [
        url(r'^admin/', include(wagtailadmin_urls)),
        url(r'^documents/', include(wagtaildocs_urls)),

        url(r'^sitemap.xml$', sitemap),

        url(r"pandas", views.Table, name="table"),

        url(r'^accounts/', include('allauth.urls')),

        # For anything not caught by a more specific rule above, hand over to
        # Wagtail's page serving mechanism. This should be the last pattern in
        # the list:
        url(r'', include(wagtail_urls)),

        # Alternatively, if you want Wagtail pages to be served from a subpath
        # of your site, rather than the site root:
        #    url(r'^pages/', include(wagtail_urls)),

    ]

if settings.DEBUG:
    import debug_toolbar

    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    from django.urls import include, path

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns 