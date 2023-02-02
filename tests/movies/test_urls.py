from django.test import SimpleTestCase
from django.urls import reverse, resolve
from apps.movies.views import MovieView, MovieDetailView
from django.test import Client

class TestUrls(SimpleTestCase):
    databases = '__all__'
    def test_base_url_is_resolved(self):
        """Testcase for simple url = ''"""
        client = Client()
        url = reverse('movies')
        response = client.get(url)

        self.assertEquals(response.status_code, 200)
