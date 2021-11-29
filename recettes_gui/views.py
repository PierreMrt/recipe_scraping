from django.shortcuts import render
from .forms import SearchForm
from django.http import HttpResponseRedirect

from .models import Recipe

def index(request):
    return render(request, 'index.html')

def az(request):
    return render(request, 'az.html')

def update(request):
    Recipe.scrap()
    return render(request, 'update.html')

def get_search(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    return render(request, 'index.html', {'form': form})