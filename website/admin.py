from django.contrib import admin
from .models import movieList, actorList

admin.site.register(movieList)
admin.site.register(actorList)