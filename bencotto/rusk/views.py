from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login as authlogin
from bencotto.rusk.models import rusk, likes, comments
from bencotto.rusk.forms import RuskForm

@login_required
def profile(request):
    return render_to_response('user_logged_in.html', {'user':request.user}, context_instance=RequestContext(request))

def home(request):
    if request.user.is_authenticated():
        return profile(request)
    else:
        randomRusks = rusk.objects.all()
        return render_to_response('home.html', {'rusks': randomRusks}, context_instance=RequestContext(request))

@login_required
def add(request):
    if request.method == 'POST': # If the form has been submitted...
        form = RuskForm(request.POST, request.FILES) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            #The default file upload handlers have put the file in MEDIA_ROOT + <upload_to>; request.FILES['image'] is an instance of UploadedFile)
            #@todo Now the data should be handled futher (scale, move, etc...)
            rusk = form.save(commit=False)
            rusk.user = request.user
            rusk.save()
            return HttpResponseRedirect('/list')
    else:
        form = RuskForm() # An unbound form

    return render_to_response('add.html', {'form': form,}, context_instance=RequestContext(request))

@login_required
def list(request):
    r = rusk.objects.all()
    return render_to_response('home.html', {'rusks': r}, context_instance=RequestContext(request))