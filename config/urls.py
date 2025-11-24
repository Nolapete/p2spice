from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView
from django.apps import apps

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("landing.urls")),
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico', permanent=True)),
    path("i18n/", include("django.conf.urls.i18n")),
    path("shop/", include(apps.get_app_config("oscar").urls[0])),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    # Append the debug toolbar URLs to the existing list
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
