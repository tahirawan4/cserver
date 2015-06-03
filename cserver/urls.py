from django.conf.urls import patterns, include, url

from django.contrib import admin
from cserver import settings
admin.autodiscover()

urlpatterns = patterns('quotes.views',
    # Examples:
    # url(r'^$', 'cserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^authors/','authors',name='authors'),
    url(r'^catgories/','catgories',name='catgories'),
    url(r'^quotes/','quotes',name='quotes'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
)
