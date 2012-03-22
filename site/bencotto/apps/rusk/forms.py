from django.forms import ModelForm
from rusk.models import rusk, likes

class RuskForm(ModelForm):
    class Meta:
        model = rusk
        fields = ('title', 'description', 'image')

class LikeForm(ModelForm):
    class Meta:
        model = likes
