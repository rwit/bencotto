from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'rusk.views.home'),
    url(r'^login', login, {'template_name': 'login.html'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/logout/$', logout),
    url(r'^logout/$', logout),
    url(r'^accounts/profile/$', 'rusk.views.profile'),
    url(r'^add', 'rusk.views.add'),
    url(r'^list', 'rusk.views.list')
)

