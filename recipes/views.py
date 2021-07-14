import pdb
from django.http import HttpResponse, JsonResponse
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
        try:
            form_data = request.POST.dict()
            image_data = request.FILES.get('image')

            success, serialized_data = RecipeSerializer(form_data=form_data)

            if not (success and image_data):
                response = {
                    "success": False,
                    "message": "All fields are mandatory."
                }
                return JsonResponse(response, status=200)


            recipe = Recipe(
                title=serialized_data['title'],
                description=serialized_data['description'],
                instructions=serialized_data['instructions'],
                cooking_time=serialized_data['cooking_time'],
                preparation_time=serialized_data['cooking_time'],
            )
            pdb.set_trace()
            recipe.save()

            for n, q in serialized_data['ingredients']:
                i = Ingredient(name=n, quantity=q)
                i.save()
                recipe.ingredients.add(i)

            image_data.name = f"{recipe.title}_image.png"
            recipe.image = image_data
            recipe.save()

            response = {
                "success": True,
                "message": "Failed to Create Recipe",
                "redirect": "/recipes/1/"
            }
            return JsonResponse(response, status=201)
        except:
            response = {
                "success": False,
                "message": "Failed to Create Recipe"
            }
            return HttpResponse(response, status=500)


def get_all_recipes(request, page: int):
    if request.method == "GET":

        chunk = 10
        start_index = (page-1) * chunk
        end_index = page * chunk

        recipes = Recipe.objects.all().order_by('-created_at')[start_index:end_index]

        context = {
            'recipes': recipes
        }
        return render(request, template_name="view_all_recipes.html", context=context)






















