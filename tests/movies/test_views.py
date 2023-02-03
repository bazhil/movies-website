import pytest
from django.test import TestCase, Client
from django.urls import reverse
from apps.movies.models import Movie, MovieShots, Actor, Category, Reviews


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.movies_url = reverse('movies')
        self.movie_detail_url = reverse('movie_detail', args=['some-slug'])

    def test_movies_list_GET(self):
        """Testcase for template for movie_list page"""
        response = self.client.get(self.movies_url)

        self.assertTemplateUsed(response, 'movies/movie_list.html')

    # def test_movies_detail_GET(self):
    #     """Testcase for movie_detail page"""
    #     response = self.client.get(self.movie_detail_url)
    #
    #     self.assertTemplateUsed(response, 'movie_detail.html')

