from django.urls import path
from . import views

urlpatterns = [
    path('recipes/', views.recipes, name='recipes'),
    path('recipe/<str:pk>', views.single_recipe, name='single-recipe'),
    path('create-recipe/', views.createRecipe, name='create-recipe'),
    path('update-recipe/<str:pk>', views.editRecipe, name='update-recipe'),
    path('delete-recipe/<str:pk>', views.deleteRecipe, name='delete-recipe'),
]