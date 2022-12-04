from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView

from .models import Movie
from .forms import ReviewForm

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

class AddReview(View):
    """Отзывы"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent'):
                form.parent_id = int(request.POST.get('parent'))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())
