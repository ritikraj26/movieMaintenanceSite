from django.urls import path
from . import views

urlpatterns = [
    path('movielist/', views.movieListApi, name='movie-list'),
    path('actorlist/', views.actorlistApi, name='actor-list'),
]