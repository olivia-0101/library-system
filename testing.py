from library_system import User, Library

import time

start = time.time()

library = Library()

for book in library.books.values():
    book.quantity = 0

Samantha = User(234)
library.borrow_book(Samantha, "classical mythology")

end = time.time()

print(f"Time taken to display books: {end - start} seconds.")