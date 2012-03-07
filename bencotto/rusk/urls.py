from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('rusk.views',
    url(r'^$', 'home'),
    #url(r'^accounts/profile/$', 'profile'),
    url(r'^add', 'add', name='add_rusk'),
    url(r'^popular', 'popular', name='popular'),
    url(r'^latest', 'latest', name='latest'),
    url(r'^rusks', 'rusks', name='rusks'),
    url(r'^friends', 'friends', name='friends'),
    url(r'^notifications', 'notifications', name='notifications'),
    url(r'^rusk', 'show_rusk', name='rusk'),
)
