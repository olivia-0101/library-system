
#creating the book class which features the title, author, ISBN and the quantity of the books available
class Book:
    def __init__(self, title, author, ISBN, quantity):
        self.title = title #title of the book
        self.author = author #author of the book
        self.ISBN = ISBN #ISBN of the book
        self.quantity = quantity #quantity of the book available to take out

#method that checks if the book is available - above 0 books
    def check_availability(self):
        return self.quantity > 0

#updates the quantity of the books in relation to borrowing or returning
    def update_quantity(self, quantity):
        self.quantity += quantity



#making the user class who can interact with the books
class User:
    def __init__(self, id):
        self.id = id
        self.borrowed_books = []

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
        self.users = []
        self.books = [
    Book("Classical Mythology", "Mark P. O. Morford", "0195153448", 2),
    Book("Clara Callan", "Richard Bruce Wright", "0002005018", 3),
    Book("Decision in Normandy", "Carlo D'Este", "0060973129", 4),
    Book("Flu: The Story of the Great Influenza Pandemic of 1918 and the Search for the Virus That Caused It", "Gina Bari Kolata", "0374157065", 10),
    Book("The Mummies of Urumchi", "E. J. W. Barber", "0393045218", 9),
    Book("The Kitchen God's Wife", "Amy Tan", "0399135782", 5),
    Book("What If?: The World's Foremost Military Historians Imagine What Might Have Been", "Robert Cowley", "0425176428", 8),
    Book("PLEADING GUILTY", "Scott Turow", "0671870432", 3),
    Book("Under the Black Flag: The Romance and the Reality of Life Among the Pirates", "David Cordingly", "0679425608", 1),
    Book("Where You'll Find Me: And Other Stories", "Ann Beattie", "074322678X", 5)  
]

#sorting function that sorts the library's books into alphabetical order
    def sort_books_by_title(self):
        self.books.sort(key= lambda book: book.title)

#printing all of the books in the books list
    def display_books(self):    
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.ISBN}, quantity: {book.quantity}")

#searching function that allows the user to find a book based on its title no matter whether they type in caps or not
        def search_book(self, title):
            for book in self.books:
                if book.title.lower() == title.lower():
                    return book
        return None      


library = Library() #creating the library object from the library class
library.sort_books_by_title() #calling the sorting function
library.display_books()