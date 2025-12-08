#creating the book class which features the title, author, ISBN and the quantity of the books available
class Book:
    def __init__(self, title, author, ISBN, quantity):
        self.title = title #title of the book
        self.author = author #author of the book
        self.ISBN = ISBN #ISBN of the book
        self.quantity = quantity #quantity of the book available to take out

Book = ["hello", "hello", "hello", "hello"]

print(Book)