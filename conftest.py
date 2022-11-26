import pytest
from pytest_factoryboy import register
from tests.factories import MovieFactory, ActorFactory, GenreFactory, CategoryFactory, ReviewsFactory, \
    RatingFactory, RatingStarFactory

register(MovieFactory)
register(ActorFactory)
register(GenreFactory)
register(CategoryFactory)
register(ReviewsFactory)
register(RatingFactory)
register(RatingStarFactory)


@pytest.fixture
def base_movie(db, movie_factory):
    new_movie = movie_factory.create('Терминатор')
    return new_movie


@pytest.fixture
def base_actor(db, actor_factory):
    new_actor = actor_factory.create('Арнольд Шварценеггер')
    return new_actor

@pytest.fixture
def base_genre(db, genre_factory):
    new_genre = genre_factory.create('Комедийный боевик')
    return new_genre

@pytest.fixture
def base_category(db, genre_category):
    new_category = genre_category.create('Криминальная комедия')
    return new_category

@pytest.fixture
def base_movies_shorts(db, movies_shorts_factory):
    new_movies_shorts = movies_shorts_factory.create('Сцена в лифте')
    return new_movies_shorts

@pytest.fixture
def base_rating_star(db, rating_star_factory):
    new_rating_star = rating_star_factory.create(3)
    return new_rating_star

@pytest.fixture
def base_rating(db, rating_factory):
    new_rating = rating_factory.create('0.0.0.0')
    return new_rating

@pytest.fixture
def base_reviews(db, reviews_factory):
    new_reviews = reviews_factory.create('123@mail.ru')
    return new_reviews
