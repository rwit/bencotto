#from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login as authlogin
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from bencotto.rusk.models import rusk, likes, comments
from bencotto.rusk.forms import RuskForm

#@login_required
#def profile(request):
#    return render_to_response('user_logged_in.html', {'user':request.user}, context_instance=RequestContext(request))
#
def home(request):
    """main landing page; simply redirects to popular"""
    return HttpResponseRedirect('/popular')

#    if request.user.is_authenticated():
#        return profile(request)
#    else:
#        randomRusks = rusk.objects.all()
#        return render_to_response('home.html', {'rusks': randomRusks}, context_instance=RequestContext(request))

def popular(request):
    """popularity is indicated by the number of views"""
    allRusks = rusk.objects.all().order_by('-views')
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    paginator = Paginator(allRusks, 3)
    try:
        rusks = paginator.page(page)
    except InvalidPage:
        rusks = paginator.page(1)
    except EmptyPage:
        rusks = paginator.page(paginator.num_pages)
    return render_to_response('list.html', {'rusks': rusks, 'title': 'Most popular rusks'}, context_instance=RequestContext(request))

def latest(request):
    """latest indicated by date added"""
    allRusks = rusk.objects.all().order_by('-date_added')
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    paginator = Paginator(allRusks, 3)
    try:
        rusks = paginator.page(page)
    except InvalidPage:
        rusks = paginator.page(1)
    except EmptyPage:
        rusks = paginator.page(paginator.num_pages)
    return render_to_response('list.html', {'rusks': rusks, 'title': 'The latest rusks'}, context_instance=RequestContext(request))

def show_rusk(request, ruskId):
    """Display a single rusk in full detail"""
    try:
        ruskId = int(ruskId)
    except ValueError:
        raise Http404()
    singleRusk = rusk.objects.get(id=ruskId)
    return render_to_response('rusk.html', {'singleRusk': singleRusk}, context_instance=RequestContext(request))

@login_required
def add(request):
    if request.method == 'POST': # If the form has been submitted...
        form = RuskForm(request.POST, request.FILES) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            rusk = form.save(commit=False) #saves cleaned data into model instance; the image field gets assigned the InMemoryUploadedFile object
            rusk.user = request.user
            rusk.save() 
            return HttpResponseRedirect('/latest')
    else:
        form = RuskForm() # An unbound form

    return render_to_response('add.html', {'form': form,}, context_instance=RequestContext(request))

@login_required
def rusks(request):
    r = rusk.objects.all()
    return render_to_response('home.html', {'rusks': r}, context_instance=RequestContext(request))

@login_required
def friends(request):
    r = rusk.objects.all()
    return render_to_response('home.html', {'rusks': r}, context_instance=RequestContext(request))

@login_required
def notifications(request):
    """Lists the notifications; user likes, user follows, ..."""
    r = rusk.objects.all()
    return render_to_response('home.html', {'rusks': r}, context_instance=RequestContext(request))
