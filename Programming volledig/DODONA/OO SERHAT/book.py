class Book:

    def __init__(self, fname, fpages, fisbnummer):
        self.name = fname
        self.pages = fpages
        self.isbnummer = fisbnummer

    def has_more_pages (self, book): 
          return self.pages > book.pages

    def __eq__(self, other):
        return self.isbnummer == other.isbnummer

    def __str__(self):
        return f"The name of the book is {self.name}, this book has {self.pages} and has as isbnummer {self.isbnummer}."