from django.db.models import Q
from .models import *
from recipes.models import Recipe, Cuisine
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def searchProfiles(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        
 
    cuisine = Cuisine.objects.filter(name__icontains=search_query)
    profiles = Profile.objects.distinct().filter(Q(name__icontains=search_query) | Q(location__icontains=search_query) |Q(cuisine__in=cuisine))

    return profiles, search_query

def paginationProfiles(request, profiles, results):
    page = request.GET.get('page')
    result = results
    paginator = Paginator(profiles, result)
    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)


    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex,rightIndex)

    return custom_range, profiles


