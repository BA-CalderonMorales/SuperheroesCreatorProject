from django.forms import ModelForm
from .models import SuperHeroes


class SuperHeroForm(ModelForm):
    class Meta:
        model = SuperHeroes
        fields = '__all__'
