class Book:

    def __init__(self, fname, fpages, fisbnummer):
        self.name = fname
        self.pages = fpages
        self.isbnummer = fisbnummer

    def has_more_pages(self, book):
        return self.pages 
    
    