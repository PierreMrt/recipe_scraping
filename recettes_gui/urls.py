from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('az/', views.AllRecipeView.as_view()),
    path('update/', views.update, name='update'),
    path('random/', views.RandomRecipeView.as_view()),
    path('search/', views.SearchView.as_view(), name='search'),
]