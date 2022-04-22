from django.urls import path
from . import views

urlpatterns = [
    path('movie/', views.movieApi, name='movie-list'),
    path('actor/', views.actorApi, name='actor-list'),
]