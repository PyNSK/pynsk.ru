from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView

from .settings import STATIC_ROOT, ROOT_PATH


admin.autodiscover()

handler500 = TemplateView.as_view(template_name="500.html")


blog_urls = [
    url(r'^', include('zinnia.urls.capabilities')),
    url(r'^search/', include('zinnia.urls.search')),
    url(r'^sitemap/', include('zinnia.urls.sitemap')),
    url(r'^trackback/', include('zinnia.urls.trackback')),
    url(r'^blog/tags/', include('zinnia.urls.tags')),
    url(r'^blog/feeds/', include('zinnia.urls.feeds')),
    url(r'^blog/random/', include('zinnia.urls.random')),
    url(r'^blog/authors/', include('zinnia.urls.authors')),
    url(r'^blog/categories/', include('zinnia.urls.categories')),
    url(r'^blog/comments/', include('zinnia.urls.comments')),
    url(r'^blog/', include('zinnia.urls.entries')),
    url(r'^blog/', include('zinnia.urls.archives')),
    url(r'^blog/', include('zinnia.urls.shortlink')),
    url(r'^blog/', include('zinnia.urls.quick_entry'))
]

urlpatterns = patterns('',
    url(r'^(favicon.ico)$', 'django.views.static.serve', {'document_root': STATIC_ROOT}),
    url(r'^(robots.txt)$', 'django.views.static.serve', {'document_root': STATIC_ROOT}),
    url(r'^humans.txt$', 'django.views.static.serve', {'document_root': ROOT_PATH, 'path': 'AUTHORS.txt'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'gnfdgdsf', include('apps.meetup.urls', namespace='meetup')),
    url(r'hgfhfdghfghf', include('apps.frontend.urls', namespace='frontend')),
    url(r'', include('apps.tasks.urls', namespace='tasks')),
    url(r'^(?P<filename>[\w-]+\.(?:html|txt))$', 'apps.meetup.views.confirm_ownership', name='ownership'),
    # url(r'^weblog/', include('zinnia.urls', namespace='zinnia')),
    # url(r'^', include(blog_urls, namespace='zinnia')),
    url(r'^comments/', include('django_comments.urls')),
)




urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
