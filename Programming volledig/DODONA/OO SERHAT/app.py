from course2 import Course
from book import Book

book1 = Book ("Impossible", 203,453234) 
book2 = Book ("Python",124,453234)
course1 = Course("Java Programming", book1) 
course2 = Course("Java Programming", book2)

print(course1)
print(course2)

print(book1 == book2)

print(course1.course_book == course2.course_book and course1.name == course2.name)

print(course1 == course2)

print(course1 is course2)

print(course1 in [course2])

print(book1.__class__)
