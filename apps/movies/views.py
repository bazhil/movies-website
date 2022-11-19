from django.shortcuts import render
from django.views import View

from .models import Movie


class MovieView(View):
    """List of movies"""
    def get(self, request):
        movie_list = Movie.objects.all()

        return render(request, 'movies.html', {'movie_list': movie_list})

