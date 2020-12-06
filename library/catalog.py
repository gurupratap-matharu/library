class Catalog:
    def __init__(self):
        """
        Initializes a catalog with empty library items.
        """
        self.library_items = []

    def search(self, query):
        """
        Searches across all library items of the catalog for a given query.
        """
        print('Searching for {} in the catalog...'.format(query))
        results = [item for item in self.library_items if item.match(query)]
        return results


class LibraryItem:
    """Represents any item in the library like a book, dvd, cd or a magazine."""

    def __init__(self, title=None, subject=None, upc=None):
        self.title = title
        self.subject = subject
        self.upc = upc

    def locate(self):
        print('child class should implement this method!!!')

    def match(self, query):
        """
        Checks if the query is a part of a library item attributes. Returns a boolean
        """
        return query in (self.subject, self.title, self.upc)


class Book(LibraryItem):
    def __init__(self, isbn, ddf):
        super().__init__()
        self.isbn = isbn
        self.ddf = ddf

    def locate(self):
        print(f'I am a book and you can find me on the shelf with DDF: {self.ddf} and ISBN: {self.isbn}.')

    def __repr__(self):
        return f'Book: DDF:{self.ddf} ISBN:{self.isbn}'


class DVD(LibraryItem):
    """
    Represents a DVD object in the library with a particular genre
    """

    def __init__(self, genre):
        self.genre = genre

    def locate(self):
        print(f'I am a dvd and you can find me on the dvd stand in the genre: {self.genre} section.')

    def __repr__(self):
        return f'DVD: Genre:{self.genre}'


class CD(LibraryItem):
    """
    Represents a CD object in the library. Most CD's are audio books with authors
    """

    def locate(self):
        print(f'I am a CD - audio book and you can find me on the CD stand.')

    def __repr__(self):
        return f'CD'


class Magazine(LibraryItem):
    """
    Represents a Magazine object in the library with a specific volume and issue which
    are used to organize the magazines in the library stand.
    """

    def __init__(self, issue, volume):
        self.issue = issue
        self.volume = volume

    def locate(self):
        print(f'I am a magazine and you can find me on the Magazine stand with \
            volume: {self.volume} issue: {self.issue}')

    def __repr__(self):
        return f'Magazine: Volume:{self.volume} Issue:{self.issue}'
