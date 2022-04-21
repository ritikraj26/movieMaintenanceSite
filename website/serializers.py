from rest_framework import serializers
from website.models import movieList, actorList

class movieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = movieList
        fields = ('title',
                  'description',
                  'releaseDate',
                  'numberOfActors',
        )
class actorlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = actorList
        fields = ('name',
                  'dateOfBirth',
                  'numberOfMovies',
                  )