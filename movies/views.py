from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from .models import Movie
from rest_framework.decorators import api_view

@api_view(['GET'])
#allows requests to limit method to what is stated.
# if not stated, it returns an error 405 (method not allowed)
def movies(request):
    data = Movie.objects.all()
    """
    can return Response(), render(), or HttpResponse
    Response() from rest_framework.response
    """
    return render(request, 'movies/movies.html', {'movies': data})

@api_view(['GET'])
def home(request):
    return HttpResponse("Home Page")

@api_view(['GET'])
def detail(request, id):
    data = Movie.objects.get(pk=id)
    return render(request, 'movies/detail.html', {'movie': data})

@api_view(['POST'])
def add(request):
    title = request.POST.get('title')
    year = request.POST.get('year')

    if title and year:
        movie = Movie(title=title, year=year)
        movie.save()
        return HttpResponseRedirect('/movies')
    return render(request, 'movies/add.html')

@api_view(['DELETE'])
def delete(request, id):
    try: movie = Movie.objects.get(pk=id)
    except: raise Http404('Movie does not exist!')
    movie.delete()
    return HttpResponseRedirect('/movies')
