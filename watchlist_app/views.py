from django.shortcuts import render
from watchlist_app.models import Movie
from django.http import JsonResponse
def movie_list(request):
    movie_list = Movie.objects.all()
    data = {
        'Movie': list(movie_list.values())
        }
    return JsonResponse(data)
def movie_details(request,pk):
    movie = Movie.objects.get(pk=pk)
    data = {
        'Name':movie.name,
        'Description':movie.description,
        'Active':movie.active
    }
    return JsonResponse(data)
    
# Create your views here.
