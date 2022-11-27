from conftest import base_movie, base_actor, base_category, base_genre, base_rating, base_reviews, \
    base_movies_shorts, base_rating_star


# Tests for Movie model
def test_movie_title():
    assert base_movie.__str__() == f'{base_movie}'

# Tests for Actor model
def test_actor_name():
    assert base_actor.__str__() == f'{base_actor}'

# Tests for Category model
def test_category_name():
    assert base_category.__str__() == f'{base_category}'

# Tests for Genre model
def test_genre_name():
    assert base_genre.__str__() == f'{base_genre}'

# Tests for RatingStar model
def test_rating_star_ip():
    assert base_rating_star.__str__() == f'{base_rating_star}'

# Tests for Rating model
def test_rating_name():
    assert base_rating.__str__() == f'{base_rating}'

# Tests for Review model
def test_review_email():
    assert base_reviews.__str__() == f'{base_reviews}'

# Tests for Movies model
def test_movies_shorts_title():
    assert base_movies_shorts.__str__() == f'{base_movies_shorts}'
