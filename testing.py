from library_system import User, Library

Mary = User(234)
library = Library()

library.borrow_book(Mary, "classical mythology")
library.return_book(Mary, "classical mythology")

for book in Mary.borrowed_books:
    print(book.title)

print(library.books)