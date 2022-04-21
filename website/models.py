from django.db import models

class movieList(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    releaseDate = models.DateField()
    numberOfActors = models.IntegerField()

    def __str__(self):
        return self.title + ' ' + self.description

class actorList(models.Model):
    name = models.CharField(max_length=200)
    dateOfBirth = models.DateField()
    numberOfMovies = models.IntegerField()

    def __str__(self):
        return self.name
