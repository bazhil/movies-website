import pytest
from pytest_factoryboy import register
from tests.factories import MovieFactory

register(MovieFactory)


@pytest.fixture
def base_movie(db, movie_factory):
    new_movie = movie_factory.create('Терминатор')
    return new_movie
