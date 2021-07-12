from django.shortcuts import render, redirect
from .forms import RecipeForm


def create_recipe(request):
    if request.method == "GET":
        form = RecipeForm()
        return render(request, 'create_recipe.html', {"form": form})
    elif request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/recipes/create')
        else:
            return render(request, 'create_recipe.html', {"form": form})
