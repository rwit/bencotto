from django.forms import ModelForm
from rusk.models import *

class RuskForm(ModelForm):
    class Meta:
        model = rusk
        fields = ('title', 'description')
        