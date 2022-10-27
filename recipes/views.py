from recipes.forms import RecipeForm, ReviewForm
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.decorators import login_required
from .utils import paginationRecipes, searchRecipes
from django.contrib import messages

def recipes(request):
    recipes, search_query = searchRecipes(request)

    custom_range, recipes = paginationRecipes(request, recipes, 6)
    
    context = {'custom_range': custom_range, 'recipes': recipes, 'search_query':search_query}
    return render(request, 'recipes/recipes.html', context)

def single_recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    cuisines = recipe.cuisine.all()
    comments = recipe.review_set.all()

    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.recipe = recipe
        review.owner = request.user.profile
        review.save()

        recipe.getVoteCount

        messages.success(request, "Your Review is successfully submitted")
        return redirect('single-recipe', pk=recipe.id)

    context = {'recipe': recipe, 'cuisines': cuisines, 'comments': comments, 'form': form}
    return render(request, 'recipes/single_recipe.html', context)

@login_required(login_url='login')
def createRecipe(request):
    profile = request.user.profile
    form = RecipeForm()

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.owner = profile
            recipe.save()
            form.save_m2m()
            return redirect('user-account')

    context = {'form': form}
    return render(request, 'recipes/recipe_form.html', context)

@login_required(login_url='login')
def editRecipe(request, pk):
    profile = request.user.profile
    recipe = profile.recipe_set.get(id=pk)
    form = RecipeForm(instance=recipe)

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        print(request.POST)
        print(request.FILES)
        if form.is_valid():
            print('reach')
            recipe_instance = form.save(commit=False)
            recipe_instance.owner = profile
            recipe_instance.save()
            form.save_m2m()
            return redirect('user-account')

    context ={'form': form}
    return render(request, 'recipes/recipe_form.html', context)


@login_required(login_url='login')
def deleteRecipe(request, pk):
    profile = request.user.profile
    recipe = profile.recipe_set.get(id=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('user-account')
    context = {'recipe': recipe}
    return render(request, 'recipes/delete.html', context)