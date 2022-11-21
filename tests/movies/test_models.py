import pytest

from apps.movies.models import Movie
from conftest import base_movie


def test_movie_title():
    """
    Test movie title string representation
    """
    assert base_movie.__str__() == f'{base_movie}'

