
from django.db import models


class Catalog(models.Model):
    name = models.CharField(max_length=60, blank=True)

    @classmethod
    def search(query):
        print('searching in catalog...')

    def __str__(self):
        return self.name


class Contributor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ContributorWithType(models.Model):
    contributor = models.ForeignKey(Contributor, related_name='contributions', on_delete=models.DO_NOTHING)
    type = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.type} - {self.contributor}'


class Genre(models.Model):
    genre = models.CharField(max_length=60)


class LibraryItem(models.Model):
    title = models.CharField(max_length=255)
    upc = models.PositiveIntegerField(verbose_name='Universal Product Code')
    subject = models.CharField(max_length=255, blank=True)
    contributors = models.ManyToManyField(ContributorWithType)
    catalog = models.ForeignKey(Catalog, on_delete=models.DO_NOTHING,
                                related_name="%(app_label)s_%(class)s_related",
                                related_query_name="%(app_label)s_%(class)ss")

    class Meta:
        abstract = True

    def locate(self):
        print(f'locating {self}...')

    def match(self, query):
        return query in (self.title, self.subject, self.upc)

    def __str__(self):
        return self.title


class Book(LibraryItem):
    isbn = models.CharField(max_length=50)
    dds = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title}\nISBN: {self.isbn}\nDDS: {self.dds}'


class CD(LibraryItem):
    def __str__(self):
        return f'CD: {self.title}'


class DVD(LibraryItem):
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return f'DVD: {self.title} Genre: {self.genre}'


class Magazine(LibraryItem):
    volume = models.CharField(max_length=50)
    issue = models.CharField(max_length=50)

    def __str__(self):
        return f'Magazine: Volume: {self.volume} Issue: {self.issue}'
