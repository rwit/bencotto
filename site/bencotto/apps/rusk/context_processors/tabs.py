import urllib
from django.core.urlresolvers import reverse, NoReverseMatch

def isActive(path, pattern):
    import re
    return re.search(pattern, path)
    
def tabs(request):
    """generate the parameters required to build the tabs"""
    tabs = []
    try:
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
    except NoReverseMatch, e:
        #Ignore exception here because tests outside Rusk do parse the global processors but don't include the Rusk urlconf
        pass 
    return dict({'tabs':tabs})
