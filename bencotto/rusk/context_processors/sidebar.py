from bencotto.rusk.models import rusk

def sidebarLikedMostRusk(request):
    #@todo: query usng joins
    r = rusk.objects.all().order_by('-date_added')[:1]
    if(r.count() == 1):
        return dict({
            'likedMostRusk': r,
        })
    else:
        #Empty dict to indicate no newest rusk available
        return dict()

def sidebarMostViewedRusk(request):
    r = rusk.objects.all().order_by('-views')[:1]
    if(r.count() == 1):
        return dict({
            'mostViewedRusk': r,
        })
    else:
        #Empty dict to indicate no newest rusk available
        return dict()

def sidebarNewestRusk(request):
    r = rusk.objects.all().order_by('-date_added')[:1]
    if(r.count() == 1):
        return dict({
            'newestRusk': r,
        })
    else:
        #Empty dict to indicate no newest rusk available
        return dict()

def sidebar(request):
    d = dict()
    d.update(sidebarLikedMostRusk(request))
    d.update(sidebarMostViewedRusk(request))
    d.update(sidebarNewestRusk(request))
    return d
