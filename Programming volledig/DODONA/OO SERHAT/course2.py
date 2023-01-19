class Course:
    def __init__(self, fname, fcourse_book): 
        self.name =  fname
        self.course_book = fcourse_book
    def __eq__(self, other):
        return self.course_book == other.course_book and self.name == other.name
    def __str__(self):
        return f'The course {self.name} follows the following book:\n{self.course_book.name}'