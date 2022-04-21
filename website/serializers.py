from rest_framework import serializers
from .models import movieList, actorList

class movieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = movieList
        fields = ('title',
                  'description',
                  'releaseDate',
                  'numberOfActors',
        )
class actorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = actorList
        fields = ('name',
                  'dateOfBirth',
                  'numberOfMovies',
        )