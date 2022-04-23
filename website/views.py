from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Movie, Actor
from .serializers import movieSerializer, actorSerializer

@csrf_exempt
def movieApi(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        movie_serializer = movieSerializer(movie, many=True)
        return JsonResponse(movie_serializer.data, safe=False)
    elif request.method == 'POST':
        movie_data = JSONParser().parse(request)
        movie_serializer = movieSerializer(data=movie_data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to add!!!", safe=False)
    elif request.method == 'PUT':
        movie_data = JSONParser().parse(request)
        movie = Movie.objects.get(title=movie_data['title'])
        movie_serializer = movieSerializer(movie, data=movie_data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return JsonResponse("Updated", safe=False)
        return JsonResponse("Failed to update", safe=False)
@csrf_exempt
def actorApi(request):
    if request.method == 'GET':
        actor = Actor.objects.all()
        actor_serializer = actorSerializer(actor, many=True)
        return JsonResponse(actor_serializer.data, safe=False)
    elif request.method == 'POST':
        actor_data = JSONParser().parse(request)
        actor_serializer = actorSerializer(data=actor_data)
        if actor_serializer.is_valid():
            actor_serializer.save()
            return JsonResponse("Addedd Successfully!", safe=False)
        return JsonResponse("Failed to add!!!", safe=False)


