import factory
from apps.movies.models import Movie, Actor
from django.db.models.signals import post_save
from faker import Factory as FakerFactory


faker = FakerFactory.create()

@factory.django.mute_signals(post_save)
class MovieFactory(factory.django.DjangoModelFactory):
    title = factory.LazyAttribute(lambda x: faker.sentence(nb_words=2))
    tagline = factory.LazyAttribute(lambda x: faker.sentence(nb_words=10))
    description = factory.LazyAttribute(lambda x: faker.sentence(nb_words=30))
    poster = factory.LazyAttribute(lambda x: faker.file_extension(category='images'))
    year = factory.LazyAttribute(lambda x: faker.year())
    country = factory.LazyAttribute(lambda x: any(['США', 'Италия', 'Англия', 'Венесуэла']))
    directors = factory.LazyAttribute(lambda x: f'{faker.first_name()} {faker.last_name()}')
    actors = factory.LazyAttribute(lambda x: f'{faker.first_name()} {faker.last_name()}')
    genres = factory.LazyAttribute(lambda x: any(['Комедия', 'Драма', 'Боевик', 'Исторический']))
    world_premiere = factory.LazyAttribute(lambda x: faker.year())
    budget = factory.LazyAttribute(lambda x: any([1000, 5000, 10000, 50000]))
    fees_in_usa = factory.LazyAttribute(lambda x: any([100000, 500000, 1000000, 5000000]))
    fees_in_world = factory.LazyAttribute(lambda x: any([100000, 500000, 1000000, 5000000]))
    category = factory.LazyAttribute(lambda x: any(['Комедия', 'Драма', 'Боевик', 'Исторический']))
    url = factory.LazyAttribute(lambda x: faker.sentence(nb_words=1))
    draft = factory.LazyAttribute(lambda x: faker.sentence(nb_words=1))

    class Meta:
        model = Movie
