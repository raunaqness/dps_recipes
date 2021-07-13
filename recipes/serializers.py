import pdb

from recipes.models import Ingredient


def RecipeSerializer(**kwargs):
    form_data = kwargs.get('form_data')
    image_data = kwargs.get('image_data')

    # try:
    payload = dict()
    payload['title'] = form_data['title']
    payload['description'] = form_data['description']
    payload['instructions'] = form_data['instructions']
    payload['preparation_time'] = float(form_data['preparation-time'])
    payload['cooking_time'] = float(form_data['cooking-time'])

    # parse ingredients
    ingredient_keys = [k for k in form_data.keys() if "ingredient-" in k]
    quantity_keys = [k for k in form_data.keys() if "quantity-" in k]

    ingredient_keys.sort()
    quantity_keys.sort()

    if len(ingredient_keys) != len(quantity_keys) or not ingredient_keys:
        print("gg")
        return False, None

    list_ingredients = []
    for index in range(len(ingredient_keys)):
        i = form_data[ingredient_keys[index]]
        q = form_data[quantity_keys[index]]
        list_ingredients.append((i, q))

    payload['ingredients'] = list_ingredients

    return True, payload

    # except:
    #     return False, None
