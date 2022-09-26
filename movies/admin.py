from .models import Movie
from django.contrib import admin

#register the database table created to the server
admin.site.register(Movie)