from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('rusk.views',
    url(r'^accounts/profile/$', 'profile'),
    url(r'^add', 'add', name='add_rusk'),
    url(r'^list', 'list', name='list_rusks'),
)
