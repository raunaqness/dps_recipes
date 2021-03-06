"""dps_recipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from recipes.views import create_recipe, get_all_recipes, get_recipe_by_id

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipe/<str:id>', get_recipe_by_id, name="get_recipe_by_id"),
    path('', get_all_recipes, name="get_all_recipes"),
    path('recipes/create', create_recipe, name="create_recipe"),
]
