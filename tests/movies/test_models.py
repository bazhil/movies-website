from unittest import TestCase

from apps.movies.models import Movie
from conftest import base_movie, base_actor, base_category, base_genre, base_rating, base_reviews, \
    base_movies_shorts, base_rating_star


# Tests for Movie model
class TestModels(TestCase):
    def test_movie_title(self):
        assert base_movie.__str__() == f'{base_movie}'

    def test_base_movie_setattr(self):
        base_movie.__setattr__('tagline', 'Test')
        assert base_movie.tagline == 'Test'

    def test_movie_class(self):
        movie = Movie()
        assert movie.title == movie.__str__()

    def test_type_movie_title(self):
        assert type(base_movie.__str__()) == str


    # Tests for Actor model
    def test_actor_name(self):
        assert base_actor.__str__() == f'{base_actor}'

    # Tests for Category model
    def test_category_name(self):
        assert base_category.__str__() == f'{base_category}'

    # Tests for Genre model
    def test_genre_name(self):
        assert base_genre.__str__() == f'{base_genre}'

    # Tests for RatingStar model
    def test_rating_star_ip(self):
        assert base_rating_star.__str__() == f'{base_rating_star}'

    # Tests for Rating model
    def test_rating_name(self):
        assert base_rating.__str__() == f'{base_rating}'

    # Tests for Review model
    def test_review_email(self):
        assert base_reviews.__str__() == f'{base_reviews}'

    # Tests for Movies model
    def test_movies_shorts_title(self):
        assert base_movies_shorts.__str__() == f'{base_movies_shorts}'
