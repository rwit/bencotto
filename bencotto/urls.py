from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login', login, {'template_name': 'login.html'}, name='login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/logout/$', logout),
    url(r'^logout/$', logout, name='logout'),
    url(r'', include('rusk.urls')), # any url matches this pattern 
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.) only for debug=True (in production should be served by apache)
    urlpatterns += patterns('',
        (r'^media_root/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
