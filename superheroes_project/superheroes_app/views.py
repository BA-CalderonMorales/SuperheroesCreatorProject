from django.shortcuts import render
from .models import SuperHeroes


# Create your views here.

def index(request):
    all_superheroes = SuperHeroes.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }
    return render(request, 'superheroes_app/index.html', context)


def detail(request, superhero_id):
    specific_hero = SuperHeroes.objects.get(pk=superhero_id)
    context = {
        'specific_hero': specific_hero
    }
    return render(request, 'superheroes_app/create.html', context)
