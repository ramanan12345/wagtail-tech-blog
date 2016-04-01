from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib import admin

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls
#May need to remove
#from wagtail.contrib.wagtailapi import urls as wagtailapi_urls

from rest_framework import routers
from blog.views import BlogPageAPIView

router = routers.DefaultRouter()
router.register(r'blog', BlogPageAPIView)

from caosblog.feed import NewestPosts
from home.views import get_articles

urlpatterns = [
    url(r'^django-admin/', include(admin.site.urls)),
    url(r'^feed/latest/$', NewestPosts()),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^api/', include(router.urls)),

    url(r'^archive/$', TemplateView.as_view(template_name='caos_archive.html'), name='archive'),
    url(r'^search/$', 'search.views.search', name='search'),
    url(r'^(?P<search_type>\w+)/(?P<search_for>[\w-]+)/$', get_articles, name="find"),

    url(r'', include(wagtail_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.views.generic import TemplateView

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
