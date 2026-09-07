from django.forms import ModelForm
from .models import Palabra

class PalabraForm(ModelForm):
    class Meta:
        model=Palabra
        fields= '__all__'
        