from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login as authlogin
from bencotto.rusk.forms import RuskForm

@login_required
def profile(request):
    return render_to_response('user_logged_in.html', {'user':request.user})

def home(request):
    if request.user.is_authenticated():
        return profile(request)
    else:
        return render_to_response('home.html')

def add(request):
    if request.method == 'POST': # If the form has been submitted...
        form = RuskForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            rusk = form.save(commit=False)
            rusk.user = request.user
            rusk.save()
            return HttpResponseRedirect('/list/')
    else:
        form = RuskForm() # An unbound form

    return render_to_response('add.html', {'form': form,})

def list(request):
    return render_to_response('home.html')
