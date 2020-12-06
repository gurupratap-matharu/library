class Catalog:
    def __init__(self):
        self.library_items = []

    def search(self):
        pass


class LibraryItem:
    """Represents any item in the library like a book, dvd, cd or a magazine."""

    def __init__(self, title=None, subject=None, upc=None):
        pass

    def locate(self):
        print('child class should implement this method!!!')


class Book(LibraryItem):
    def __init__(self, isbn, ddf):
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
