from django.forms import ModelForm
from .models import Wine

class WineForm(ModelForm):
  class Meta:
    model = Wine
    fields = ('year', 'wine')