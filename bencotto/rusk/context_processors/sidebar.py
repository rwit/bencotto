from django.db.models import Count
from bencotto.rusk.models import rusk, likes

def sidebarLikedMostRusk(request):
    #select the rusk that is likes the most using aggregation
    l = likes.objects.annotate(num_likes=Count('id')).order_by('-num_likes')[:1]
    if(l.count() == 1):
        return dict({
            'likedMostRusk': l[0].rusk,
        })
    else:
        #Empty dict to indicate no newest rusk available
        return dict()

def sidebarMostViewedRusk(request):
    r = rusk.objects.all().order_by('-views')[:1]
    if(r.count() == 1):
        return dict({
            'mostViewedRusk': r[0],
        })
    else:
        #Empty dict to indicate no newest rusk available
        return dict()

def sidebarNewestRusk(request):
    r = rusk.objects.all().order_by('-date_added')[:1]
    if(r.count() == 1):
        return dict({
            'newestRusk': r[0],
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
