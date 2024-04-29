from django.shortcuts import render, redirect
from .models import *


def recipe(request):
    if request.method == 'POST':
        data = request.POST
        recipeName = data.get('name')
        recipeDespcription = data.get('description')
        recipeImage = request.FILES.get('image')

        Recipe.objects.create(
            name = recipeName,
            description = recipeDespcription,
            image = recipeImage
        )
        return redirect('/recipes/')
    
    querySet = Recipe.objects.all()
    return render(request, 'recipe.html', {'recipes': querySet})

def delete_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/recipes/')

def update_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    if request.method == 'POST':
        data = request.POST
        recipeName = data.get('name')
        recipeDescription = data.get('description')
        recipeImage = request.FILES.get('image')

        queryset.name = recipeName
        queryset.description = recipeDescription
        if recipeImage:
            queryset.image = recipeImage
        
        queryset.save()
        return redirect('/recipes/')
    return render(request, 'update_recipe.html', {'recipe': queryset})