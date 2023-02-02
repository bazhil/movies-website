from django.test import SimpleTestCase
from django.urls import reverse, resolve
from apps.movies.views import MovieView, MovieDetailView
from django.test import Client

class TestUrls(SimpleTestCase):
    databases = '__all__'
    def setUp(self):
        self.client = Client()
        self.movies_url = reverse('movies')
        self.movie_detail_url = reverse('movie_detail', args=['some-slug'])

    def test_movies_url_response_resolves(self):
        """Testcase for movies url - check response code == 200"""
        response = self.client.get(self.movies_url)

        self.assertEquals(response.status_code, 200)

    def test_movies_url_view_resolves(self):
        """Testcase for movies url - check view class"""
        self.assertEquals(resolve(self.movies_url).func.view_class, MovieView)

    def test_movie_detail_url_resolves(self):
        """Testcase for base url = 'movies'"""

        self.assertEquals(resolve(self.movie_detail_url).func.view_class, MovieDetailView)
