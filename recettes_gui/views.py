from re import template
from django.shortcuts import render
from .forms import SearchForm
from django.http import HttpResponseRedirect
from django.views.generic import ListView

from .models import Recipe

def index(request):
    return render(request, 'index.html')

class AllRecipeView(ListView):
    model = Recipe
    context_object_name = 'all_recipes'
    template_name = 'az.html'

class RandomRecipeView(ListView):
    model = Recipe
    context_object_name = 'random_recipes'
    template_name = 'random.html'
    
    def get_queryset(self):
       return Recipe.objects.order_by('?')

def update(request):
    Recipe().scrap()
    return render(request, 'update.html')

class SearchView(ListView):
    template_name = 'search.html'
    context_object_name = 'searched_item'
    model = Recipe

    def get_queryset(self):
        query = self.request.GET.get('q')
        search_choice = self.request.GET.get('filter')
        if query:
            if search_choice == 'ingredient':
                results = Recipe.objects.filter(ingredients__icontains=query)
            elif search_choice == 'recipe':
                results = Recipe.objects.filter(name__icontains=query) 
            elif search_choice == 'both':
                results = Recipe.objects.filter(ingredients__icontains=query) | Recipe.objects.filter(name__icontains=query) 
            return results
        else:
            return Recipe.objects.all()

def recipe_details(request, pk):
    recipe = Recipe.objects.filter(id=pk, )
    context = {'recipe': recipe, }
    print(context)
    return render(request, 'recipe_details.html', context)