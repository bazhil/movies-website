from django import template
from apps.movies.models import Category, Movie

register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()

# TODO: не обнаруживается данный путь - на интерфейсе ошибка - полечить!
@register.inclusion_tag('apps/movies/templates/tags/last_movies.html')
def get_last_movies():
    movies = Movie.objects.order_by('id')[:5]
    return {'last_movies': movies}

