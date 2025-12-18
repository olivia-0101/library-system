from library_system import User, Library

Mary = User(234)
library = Library()

book_title = "classical mythology"
book = library.search_book(book_title)

if book:
    print(f"{book.title} by {book.author} is available. There are {book.quantity}.")
else:
    print("Book not found.")