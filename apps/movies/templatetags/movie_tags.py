from django import template
from apps.movies.models import Category, Movie

register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()

# TODO: так более-менее работает
@register.simple_tag()
def get_last_movies(count=5):
    movies = Movie.objects.order_by('id')[:count]

    return movies

# TODO: не обнаруживается данный путь, видимо из-за нестандартной структуры проекта
#  - внутри метода фильмы получаются, не попадают на форму, тк она не найдена
# @register.inclusion_tag('apps/movies/tags/last_movies.html')
# def get_last_movies(count=5):
#     movies = Movie.objects.order_by('id')[:count]
#
#     return movies

