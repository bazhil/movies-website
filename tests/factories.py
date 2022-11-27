import factory
from apps.movies.models import Movie, Actor, Category, Genre, MovieShots, RatingStar, Rating, Reviews
from django.db.models.signals import post_save
from faker import Factory as FakerFactory
from random import randint

faker = FakerFactory.create()


@factory.django.mute_signals(post_save)
class ActorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Actor

    name = factory.LazyAttribute(lambda x: f'{faker.first_name()} {faker.last_name()}')
    age = factory.LazyAttribute(lambda x: randint(5, 80))
    description = factory.LazyAttribute(lambda x: faker.sentence(nb_words=100))
    image = factory.LazyAttribute(lambda x: faker.file_extension(category='image'))


@factory.django.mute_signals(post_save)
class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.LazyAttribute(lambda x: any(['Комедия', 'Драма', 'Боевик', 'Исторический']))
    description = factory.LazyAttribute(lambda x: faker.sentence(nb_words=30))
    url = factory.LazyAttribute(lambda x: faker.sentence(nb_words=1))


@factory.django.mute_signals(post_save)
class GenreFactory(factory.django.DjangoModelFactory):
    name = factory.LazyAttribute(lambda x: any(['Комедия', 'Драма', 'Боевик', 'Исторический']))
    description = factory.LazyAttribute(lambda x: faker.sentence(nb_words=30))
    url = factory.LazyAttribute(lambda x: faker.sentence(nb_words=1))

    class Meta:
        model = Genre


@factory.django.mute_signals(post_save)
class RatingStarFactory(factory.django.DjangoModelFactory):
    value = factory.LazyAttribute(lambda x: any([i for i in range(6)]))

    class Meta:
        model = RatingStar


@factory.django.mute_signals(post_save)
class MovieFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Movie

    title = factory.LazyAttribute(lambda x: faker.sentence(nb_words=2))
    tagline = factory.LazyAttribute(lambda x: faker.sentence(nb_words=10))
    description = factory.LazyAttribute(lambda x: faker.sentence(nb_words=30))
    poster = factory.LazyAttribute(lambda x: faker.file_extension(category='image'))
    year = factory.LazyAttribute(lambda x: faker.year())
    country = factory.LazyAttribute(lambda x: any(['США', 'Италия', 'Англия', 'Венесуэла']))
    directors = factory.SubFactory(ActorFactory)
    actors = factory.SubFactory(ActorFactory)
    genres = factory.SubFactory(GenreFactory)
    world_premiere = faker.year()
    budget = factory.LazyAttribute(lambda x: any([1000, 5000, 10000, 50000]))
    fees_in_usa = factory.LazyAttribute(lambda x: any([100000, 500000, 1000000, 5000000]))
    fees_in_world = factory.LazyAttribute(lambda x: any([100000, 500000, 1000000, 5000000]))
    category = factory.SubFactory(CategoryFactory)
    url = factory.LazyAttribute(lambda x: faker.sentence(nb_words=1))
    draft = factory.LazyAttribute(lambda x: faker.sentence(nb_words=1))


@factory.django.mute_signals(post_save)
class ReviewsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reviews

    email = faker.safe_email()
    name = factory.LazyAttribute(lambda x: faker.sentence(nb_words=20))
    text = factory.LazyAttribute(lambda x: faker.sentence(nb_words=200))
    parent = None
    movie = factory.SubFactory(MovieFactory)


@factory.django.mute_signals(post_save)
class RatingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Rating

    ip = faker.ipv4()
    star = factory.SubFactory(RatingStarFactory)
    movie = factory.SubFactory(MovieFactory)



@factory.django.mute_signals(post_save)
class MovieShotsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MovieShots

    title = factory.LazyAttribute(lambda x: faker.sentence(nb_words=2))
    description = factory.LazyAttribute(lambda x: faker.sentence(nb_words=30))
    image = factory.LazyAttribute(lambda x: faker.file_extension(category='image'))
    movie = factory.SubFactory(MovieFactory)

