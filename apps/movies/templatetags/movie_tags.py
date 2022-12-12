from django import template
from apps.movies.models import Category, Movie

register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()

# TODO: не обнаруживается данный путь - на интерфейсе ошибка - полечить!
#  - внутри метода фильмы получаются, но видимо, не попадают на форму
@register.inclusion_tag('movies-website/apps/movies/tags/last_movies.html')
def get_last_movies(count=5):
    movies = Movie.objects.order_by('id')[:count]

    return {'last_movies': movies}
