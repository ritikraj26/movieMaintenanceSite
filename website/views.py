from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import movieList, actorList
from .serializers import movieListSerializer, actorListSerializer

@csrf_exempt
def movieListApi(request):
    if request.method == 'GET':
        movie = movieList.objects.all()
        movie_serializer = movieListSerializer(movie, many=True)
        return JsonResponse(movie_serializer.data, safe=False)
    elif request.method == 'POST':
        movie_data = JSONParser().parse(request)
        movie_serializer = movieListSerializer(data=movie_data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to add!!!", safe=False)
    # elif request.method =='PUT':
    #     movie_data = JSONParser().parse(request)
    #     movie = movieList.objects.get()
@csrf_exempt
def actorlistApi(request):
    if request.method == 'GET':
        actor = actorList.objects.all()
        actor_serializer = actorListSerializer(actor, many=True)
        return JsonResponse(actor_serializer.data, safe=False)
    elif request.method == 'POST':
        actor_data = JSONParser().parse(request)
        actor_serializer = actorListSerializer(data=actor_data)
        if actor_serializer.is_valid():
            actor_serializer.save()
            return JsonResponse("Addedd Successfully!", safe=False)
        return JsonResponse("Failed to add!!!", safe=False)


