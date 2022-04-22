from rest_framework import serializers
from .models import Movie, Actor

class movieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title',
                  'description',
                  'releaseDate',
                  'numberOfActors',
                  'upvote',
                  'downvote',
        )
class actorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('name',
                  'dateOfBirth',
                  'numberOfMovies',
        )