from library_system import User, Library

Mary = User(234)
library = Library()

book_title = "classical mythology"
Mary.borrow_book(book_title)

print(Mary.borrowed_books)