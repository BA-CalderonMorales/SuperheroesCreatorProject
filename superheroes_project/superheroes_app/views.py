from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import SuperHeroes
from .forms import SuperHeroForm
from django.contrib import messages


# Create your views here.

def index(request):
    all_superheroes = SuperHeroes.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }
    return render(request, 'superheroes_app/index.html', context)


def detail(request, superhero_id):
    """Made to assist with specific_hero.html. Will output the details from MySQL database about the
    current hero being referenced."""
    specific_hero = SuperHeroes.objects.get(pk=superhero_id)
    context = {
        'specific_hero': specific_hero
    }
    return render(request, 'superheroes_app/specific_hero.html', context)


def edit(request):
    print("Print POST: ", request.POST)
    form = SuperHeroForm(request.POST)
    if request.method == 'POST':
        form = SuperHeroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'superheroes_app/edit.html', context)


def update(request, superhero_id):
    the_hero = SuperHeroes.objects.get(pk=superhero_id)
    form = SuperHeroForm(instance=the_hero)
    if request.method == 'POST':
        form = SuperHeroForm(request.POST, instance=the_hero)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
        'the_hero': the_hero
    }
    return render(request, 'superheroes_app/edit.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_ability = request.POST.get('primary_ability')
        secondary_ability = request.POST.get('secondary_ability')
        catchphrase = request.POST.get('catchphrase')
        new_hero = SuperHeroes(
            name=name,
            alter_ego=alter_ego,
            primary_ability=primary_ability,
            secondary_ability=secondary_ability,
            catchphrase=catchphrase
        )
        new_hero.save()
        return HttpResponseRedirect(reverse('superheroes_app:index'))
    else:
        return render(request, 'superheroes_app/create.html')

