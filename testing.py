from library_system import User, Library

Mary = User(234)
library = Library()

library.borrow_book(Mary, "classical mytholog")

print(Mary.id)
for book in Mary.borrowed_books:
    print(book.title)