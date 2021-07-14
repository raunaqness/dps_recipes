import pdb

from django.shortcuts import render, redirect
from .forms import RecipeForm
from .models import Recipe, Ingredient
from .serializers import RecipeSerializer


def create_recipe(request):
    if request.method == "GET":
        form = RecipeForm()
        return render(request, 'create_recipe.html', {
            "form": form,
        })
    elif request.method == "POST":
        form_data = request.POST.dict()
        image_data = request.FILES['image']
        success, serialized_data = RecipeSerializer(form_data=form_data)

        recipe = Recipe(
            title=serialized_data['title'],
            description=serialized_data['description'],
            instructions=serialized_data['instructions'],
            cooking_time=serialized_data['cooking_time'],
            preparation_time=serialized_data['cooking_time'],
        )
        recipe.save()

        for n, q in serialized_data['ingredients']:
            i = Ingredient(name=n, quantity=q)
            i.save()
            recipe.ingredients.add(i)

        image_data.name = f"{recipe.title}_image.png"
        recipe.image = image_data
        recipe.save()
