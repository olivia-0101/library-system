from library_system import User, Library

import time

start = time.time()

Mary = User(234)
library = Library()

book_title = "classical mythology"
Mary.borrow_book(book_title)
library.display_books

end = time.time()

print(Mary.borrowed_books)
print(f"Time taken to display books: {end - start} seconds.")