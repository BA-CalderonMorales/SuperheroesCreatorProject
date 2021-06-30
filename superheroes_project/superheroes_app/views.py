from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import SuperHeroes
from .forms import SuperHeroForm
from django.contrib import messages


# Create your views here.

def index(request):
    """Allows me to access all the superheroes whenever the method is called inside
    of an HTML/CSS file. Contains all the superheroes inside of MySQL database."""
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
    """This method works in conjunction with the edit.html template. I am using ModelForm,
    which is within one of Django's libraries. In this method, when I print(..., request.POST),
    I am able to see what's inside the request. Then I am able to create a form from which I can
    access the variables inside of MySQL database containing all of my superheroes. The heroes are
    then autopopulated onto the appropriate fields within the edit.html template, wherever it is
    that I'm calling this method."""
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
    """Once I've ran the edit method above, this update method actually changes the info contained
    inside of MySQL database. The parameters inside every field of the form are changed in edit.html
    and this method allows the communication between MySQL and the current superhero being updated to
    actually update on the database. Once the method is complete, the screen will return to the main
    screen."""
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
    """This method allows a user to create a superhero to their liking. They are able to update the
    current MySQL database in existence with this method. Will add a superhero created to the end of
    the list of current superheroes."""
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


def delete(superhero_id):
    """Simply allows a user to delete a superhero from the current MySQL database containing all heroes."""
    SuperHeroes.objects.filter(id=superhero_id).delete()
    return HttpResponseRedirect(reverse('superheroes_app:index'))
