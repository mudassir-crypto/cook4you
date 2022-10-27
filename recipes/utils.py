from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

def searchRecipes(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        
 
    cuisine = Cuisine.objects.filter(name__icontains=search_query)
    owner = Profile.objects.filter(name__icontains=search_query)
    recipes = Recipe.objects.distinct().filter(Q(title__icontains=search_query) | Q(cuisine__in=cuisine) | Q(owner__in=owner))

    return recipes, search_query

def paginationRecipes(request, recipes, results):
    page = request.GET.get('page')
    result = results
    paginator = Paginator(recipes, result)
    try:
        recipes = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        recipes = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        recipes = paginator.page(page)


    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex,rightIndex)

    return custom_range, recipes