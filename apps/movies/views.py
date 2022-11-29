from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Movie


class MovieView(ListView):
    """List of movies"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'movie_list.html'


class MovieDetailView(DetailView):
    """Описание фильма"""

    model = Movie
    slug_field = 'url'
    template_name = 'movie_detail.html'

