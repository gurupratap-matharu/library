import factory
from catalog.models import CD, DVD, Book, Catalog, Genre, Magazine


class CatalogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Catalog
        django_get_or_create = ('name',)

    name = 'FCAGLP'


class GenreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Genre
        django_get_or_create = ('genre',)

    genre = factory.Faker('word')


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book
    title = factory.Faker('catch_phrase')
    subject = factory.Faker('word')
    catalog = factory.SubFactory(CatalogFactory)
    isbn = factory.Faker('isbn13')
    dds = factory.Faker('uuid4')
    upc = factory.Faker('ean13')


class CDFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CD
    title = factory.Faker('catch_phrase')
    upc = factory.Faker('ean13')
    subject = factory.Faker('word')
    catalog = factory.SubFactory(CatalogFactory)


class DVDFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DVD
    title = factory.Faker('catch_phrase')
    upc = factory.Faker('ean13')
    subject = factory.Faker('word')
    catalog = factory.SubFactory(CatalogFactory)
    genre = factory.SubFactory(GenreFactory)


class MagazineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Magazine

    title = factory.Faker('catch_phrase')
    upc = factory.Faker('ean13')
    subject = factory.Faker('word')
    catalog = factory.SubFactory(CatalogFactory)

    volume = factory.Faker('uuid4')
    issue = factory.Faker('ean13')
