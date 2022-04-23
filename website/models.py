from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    releaseDate = models.DateField()
    numberOfActors = models.IntegerField()
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Actor(models.Model):
    name = models.CharField(max_length=200)
    dateOfBirth = models.DateField()
    numberOfMovies = models.IntegerField()
    movie = models.ForeignKey(Movie, default=1, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.name
