from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cakeandmidgets.views.home', name='home'),
    url(r'^$', 'comics.views.home'), 
    url(r'^random$', 'comics.views.random'), 
    url(r'^more$', 'comics.views.archive'), 
    url(r'^deploy$', 'comics.views.deploy'), 
    url(r'^comic/(?P<comic_name>\w+)/$', 'comics.views.comic'),

    (r'^comments/', include('django.contrib.comments.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

import os
from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('', url(r'^media/(.*)$', 'django.views.static.serve', kwargs={'document_root': os.path.join(settings.PROJECT_PATH, 'media')}), )
