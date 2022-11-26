from conftest import base_movie, base_actor, base_category, base_genre, base_rating, base_reviews, \
    base_movies_shorts, base_rating_star


def test_movie_title():
    assert base_movie.__str__() == f'{base_movie}'

def test_actor_name():
    assert base_actor.__str__() == f'{base_actor}'

def test_category_name():
    assert base_category.__str__() == f'{base_category}'

def test_genre_name():
    assert base_genre.__str__() == f'{base_genre}'

def test_rating_star_ip():
    assert base_rating_star.__str__() == f'{base_rating_star}'

def test_rating_name():
    assert base_rating.__str__() == f'{base_rating}'

def test_review_email():
    assert base_reviews.__str__() == f'{base_reviews}'

def test_movies_shorts_title():
    assert base_movies_shorts.__str__() == f'{base_movies_shorts}'
