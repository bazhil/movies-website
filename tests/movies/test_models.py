import pytest
from PIL.Image import Image
import factory
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile, SimpleUploadedFile
from django.test import TestCase
from apps.movies.models import Movie, Actor, Category, Genre
from conftest import base_movie


def test_movie_title():
    """
    Test movie title string representation with pytest
    """
    assert base_movie.__str__() == f'{base_movie}'


class MovieModelTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    @classmethod
    def setUpTestData(cls):
        Movie.objects.create(
            title='Брат',
            tagline='Сила в Правде!',
            description='Крутой фильм',
            poster=SimpleUploadedFile(name='test_image.jpg',
                                      content=File(file=b""),
                                      content_type='image/jpeg'),
            year=1998,
            country='Russia',
            directors=Actor.objects.create(name='Сергей Бодров',
                                           age=34,
                                           description='Культовая роль культового актера',
                                           image=SimpleUploadedFile(name='test_image_2.jpg',
                                                                    content=File(file=b""),
                                                                    content_type='image/jpeg'),),
            actors=Actor.objects.create(name='Алексей Балабанов',
                                        age=45,
                                        description='Культовый режиссер',
                                        image=SimpleUploadedFile(name='test_image_3.jpg',
                                                                 content=File(file=b""),
                                                                 content_type='image/jpeg'),),
            genres=Genre.objects.create(name='Боевик',
                                        description='Стреляют, убивают',
                                        url='action'),
            world_premiere=1998,
            budget=1,
            fees_in_usa=1,
            fees_in_world=1,
            category=Category.objects.create(name='Боевик',
                                             description='Стреляют, убивают',
                                             url='action'),
            url='brat',
            draft=None
        )

    def test_movie_title(self):
        movie = Movie.objects.get(id=1)
        self.assertEqual(movie.title, 'Брат')

    def test_movie_tagline(self):
        movie = Movie.objects.get(id=1)
        self.assertEqual(movie.tagline, 'Сила в Правде!')
