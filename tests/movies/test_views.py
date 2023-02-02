import pytest
from django.test import TestCase, Client
from django.urls import reverse
from apps.movies.models import Movie, MovieShots, Actor, Category

class TestViews(TestCase):
    def test_movies_list_GET(self):
        client = Client()
        response = client.get(reverse('movies'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'apps/movies/templates/movies/movie_list.html')
