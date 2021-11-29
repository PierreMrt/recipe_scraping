from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('az', views.az, name='az'),
    path('update', views.update, name='update'),
]