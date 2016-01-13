import mezzanine_pagedown.urls
from django.conf import settings as dj_settings
from django.conf.urls import include, url
from django.conf.urls import patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.i18n import set_language
from mezzanine.conf import settings
from mezzanine.core.views import direct_to_template

admin.autodiscover()

urlpatterns = patterns(
        '',
        url("^pagedown/", include(mezzanine_pagedown.urls)),
        url(r'^(favicon.ico)$', 'django.views.static.serve', {'document_root': dj_settings.STATIC_ROOT}),
        url(r'^(robots.txt)$', 'django.views.static.serve', {'document_root': dj_settings.STATIC_ROOT}),
        url(r'^humans.txt$', 'django.views.static.serve',
            {'document_root': dj_settings.ROOT_PATH, 'path': 'AUTHORS.txt'}),
        url(r'^admin/', include(admin.site.urls)),

        # url(r'gnfdgdsf', include('apps.meetup.urls', namespace='meetup')),
        url(r'hgfhfdghfghf', include('apps.frontend.urls', namespace='frontend')),
        url(r'', include('apps.tasks.urls', namespace='tasks')),
        url(r'^daily/', include('apps.dailydigest.urls', namespace='dailydigest')),

        # url(r'^comments/', include('django_comments.urls')),
)

if settings.USE_MODELTRANSLATION:
    urlpatterns += [
        url('^i18n/$', set_language, name='set_language'),
    ]

urlpatterns += [

    url("^blog$", direct_to_template, {"template": "index.html"}, name="home"),
    url("^blog/", include("mezzanine.urls")),
]

# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.
handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
