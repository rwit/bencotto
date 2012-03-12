from django.db.models import Count
from bencotto.rusk.models import rusk, likes

def sidebarLikedMostRusk(request):
    #select the rusk that is liked the most using aggregation
    #notice the model query api inserts group_by's for fields that are not meant to be grouped
    #l = likes.objects.annotate(num_likes=Count('rusk__id')).order_by('-num_likes') \
    #    .values('rusk__id', 'rusk__title', 'rusk__image', 'rusk__date_added', 'rusk__user__username', 'num_likes')[:1]
    r = rusk.objects.raw( 
        'SELECT ' +
        '"rusk_rusk"."id", "rusk_rusk"."title", "rusk_rusk"."image", "rusk_rusk"."date_added", ' +
        '"rusk_likes"."rusk_id", ' +
        'T4."username", COUNT("rusk_likes"."rusk_id") AS "num_likes" ' +
        'FROM ' +
        '"rusk_rusk" ' +
        'INNER JOIN "rusk_likes" ON ("rusk_likes"."rusk_id" = "rusk_rusk"."id") ' +
        'INNER JOIN "auth_user" T4 ON ("rusk_rusk"."user_id" = T4."id") ' +
        'GROUP BY "rusk_likes"."rusk_id" ' +
        'ORDER BY "num_likes" DESC LIMIT 1')

    try:
        return dict({
            'likedMostRusk': dict({
                'rusk':r[0], #Only issue here is that the returned object is in fact not a rusk but contains referenced items like rusk__title
            })
        })
    except IndexError:
        #Empty dict to indicate no newest rusk available
        return dict()

def sidebarMostViewedRusk(request):
    r = rusk.objects.all().order_by('-views')[:1]
    try:
        return dict({
            'mostViewedRusk': dict({
                'rusk':r[0],
            })
        })
    except IndexError:
        #Empty dict to indicate no newest rusk available
        return dict()

def sidebarNewestRusk(request):
    r = rusk.objects.all().order_by('-date_added')[:1]
    try:
        return dict({
            'newestRusk': dict({
                'rusk':r[0],
            })
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
