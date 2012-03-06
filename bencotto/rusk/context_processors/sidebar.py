from django.db.models import Count
from bencotto.rusk.models import rusk, likes

def sidebarLikedMostRusk(request):
    #select the rusk that is liked the most using aggregation
    l = likes.objects.annotate(num_likes=Count('id')).order_by('-num_likes').values('rusk__title', 'rusk__description', 'num_likes')[:1]
    #SELECT "rusk_rusk"."title", "rusk_rusk"."description", COUNT("rusk_likes"."id") AS "num_likes" 
    #FROM "rusk_likes" 
    #INNER JOIN "rusk_rusk" ON ("rusk_likes"."rusk_id" = "rusk_rusk"."id") 
    #GROUP BY "rusk_likes"."id", "rusk_likes"."user_id", "rusk_likes"."rusk_id", "rusk_rusk"."title", "rusk_rusk"."description" 
    #ORDER BY "num_likes" 
    #DESC LIMIT 1    
    try:
        return dict({
            'likedMostRusk': l[0], #Only issue here is that the returned object is in fact not a rusk but contains referenced items like rusk__title
        })
    except IndexError:
        #Empty dict to indicate no newest rusk available
        return dict()

def sidebarMostViewedRusk(request):
    r = rusk.objects.all().order_by('-views')[:1]
    try:
        return dict({
            'mostViewedRusk': r[0],
        })
    except IndexError:
        #Empty dict to indicate no newest rusk available
        return dict()

def sidebarNewestRusk(request):
    r = rusk.objects.all().order_by('-date_added')[:1]
    try:
        return dict({
            'newestRusk': r[0],
        })
    except IndexError:
        #Empty dict to indicate no newest rusk available
        return dict()

def sidebar(request):
    d = dict()
    d.update(sidebarLikedMostRusk(request))
    d.update(sidebarMostViewedRusk(request))
    d.update(sidebarNewestRusk(request))
    return d
