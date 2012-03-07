import logging
import urllib
from django.core.urlresolvers import reverse

#logger = logging.getLogger(__name__)

def isActive(path, pattern):
    import re
    return re.search(pattern, path)
    
def tabs(request):
    """generate the parameters required to build the tabs"""
    tabs = []
    tabs.append(dict({ 'title':'Popular rusks', 'link':reverse('popular'), 'is_active':isActive(request.path, 'popular')}))
    tabs.append(dict({ 'title':'Latest rusks', 'link':reverse('latest'), 'is_active':isActive(request.path, 'latest')}))
    if request.user.is_authenticated():
        tabs.append(dict({ 'title':'Add a rusk', 'link':reverse('add_rusk'), 'is_active':isActive(request.path, 'add')}))
        tabs.append(dict({ 'title':'My rusks', 'link':reverse('rusks'), 'is_active':isActive(request.path, 'rusks')}))
        tabs.append(dict({ 'title':'My friends rusks', 'link':reverse('friends'), 'is_active':isActive(request.path, 'friends')}))
        tabs.append(dict({ 'title':'Notifications', 'link':reverse('notifications'), 'is_active':isActive(request.path, 'notifications')}))
        tabs.append(dict({ 'title':'Logout', 'link':reverse('logout'), 'is_active':isActive(request.path, 'logout')}))
    else:
        tabs.append(dict({ 'title':'Login', 'link':reverse('login') + '?' + urllib.urlencode({'next':'popular'}), 'is_active':isActive(request.path, 'login')}))
    return dict({'tabs':tabs})
