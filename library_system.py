import csv

#creating the book class which features the title, author, ISBN and the quantity of the books available
class Book:
    def __init__(self, title, author, ISBN):
        self.title = title #title of the book
        self.author = author #author of the book
        self.ISBN = ISBN #ISBN of the book

#method that checks if the book is available - above 0 books
    def check_availability(self):
        return self.quantity > 0

#updates the quantity of the books in relation to borrowing or returning
    def update_quantity(self, quantity):
        self.quantity += quantity



#making the user class who can interact with the books
class User:
    def __init__(self, id): #only has an ID as an attribute
        self.id = id
        self.borrowed_books = [] #the user stores their borrowed books

#giving the user class the ability to borrow books, and adding it to their list of borrowed books
    def borrow_book(self, book):
        self.borrowed_books.append(book)

#giving the user class the ability to return books, removing it from their list of borrowed books
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)



#creating the library class that stores all of the books and users
class Library:
    def __init__(self):
        self.users = [] #the library stores all of the users
        self.books = {} #the library stores all of the books
        with open("library.csv", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=';')

            for i, row in enumerate(reader):
                if i >= 100:
                    break
                
                title_key = row["Title"].lower()

                self.books[title_key] = Book(
                    row["Title"],
                    row["Author"],
                    row["ISBN"],
                )


#printing all of the books in the books list
    def display_books(self):    
        for title in sorted(self.books.keys()):
            book = self.books[title]
            print(
                f"Title: {book.title}, "
                f"Author: {book.author}, "
                f"ISBN: {book.ISBN}, "
                f"Quantity: {book.quantity}"
            ) #prints 

    def list_books(self):
        if self.books:
            print("Books:")

#searching function that allows the user to find a book based on its title no matter whether they type in caps or not
    def search_book(self, title):
        return self.books.get(title.lower())

#borrowing function that allows the user to borrow a book based on its title
    def borrow_book(self, user, title): #defines that the user is borrowing the book by its title
        book = self.search_book(title) #the library looks through its list
        if not book: #checks if the search fails
            print("Book not found.") #prints an error message letting the user know the book cannot be found
            return #stops the function
        if not book.check_availability(): #checks if any of the books are available
            print("Book unavailable.") #prints an error message letting the user know there are none of those books left
            return #stops the function
        
        user.borrow_book(book) #calls the user's borrowing book method
        book.update_quantity(-1) #updates the book list by removing one

#returning function that allows the user to return a book to the library based on its title
    def return_book(self, user, title): #defines that the user is returning the book by its title
        title = title.lower()
        for book in user.borrowed_books:
            if book.title.lower() == title:
                user.return_book(book) #calls the method
                book.update_quantity(1) #updates the book list by adding one
                print(f"{book.title} has been successfully returned to the library.") #prints a message stating that the book has been returned to the library
                return #stops the function
        
        print("User has not borrowed this book.") #if the book cannot be found, print this message

#library interface
print("Welcome to the Library! Here you can:")
print("1. Borrow Books")
print("2. Return Books")
print("3. Search for Books")
print("Below are the books currently available in the library.")
    

library = Library() #creating the library object from the library class
library.list_books() #listing the books
library.display_books() #calling the displaying of the books beneath the list