from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', login, {'template_name': 'login.html'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/profile/$', 'rusk.views.profile')
)

