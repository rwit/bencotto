from django.forms import ModelForm
from bencotto.rusk.models import rusk

class RuskForm(ModelForm):
    class Meta:
        model = rusk
        fields = ('title', 'description', 'image')
        