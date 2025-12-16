
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
        self.books = { #the library stores all of the books
            "classical mythology": Book("Classical Mythology", "Mark P. O. Morford", "0195153448", 2),
            "clara callan": Book("Clara Callan", "Richard Bruce Wright", "0002005018", 3),
            "decision in normandy": Book("Decision in Normandy", "Carlo D'Este", "0060973129", 4),
            "flu: the story of the great influenza pandemic of 1918 and the search for the virus that caused it": Book("Flu: The Story of the Great Influenza Pandemic of 1918 and the Search for the Virus That Caused It", "Gina Bari Kolata", "0374157065", 10),
            "the mummies of urumchi": Book("The Mummies of Urumchi", "E. J. W. Barber", "0393045218", 9),
            "the kitchen god's wife": Book("The Kitchen God's Wife", "Amy Tan", "0399135782", 5),
            "what if?: the world's foremost military historians imagine what might have been": Book("What If?: The World's Foremost Military Historians Imagine What Might Have Been", "Robert Cowley", "0425176428", 8),
            "pleading guilty": Book("PLEADING GUILTY", "Scott Turow", "0671870432", 3),
            "under the black flag: the romance and the reality of life among the pirates": Book("Under the Black Flag: The Romance and the Reality of Life Among the Pirates", "David Cordingly", "0679425608", 1),
            "where you'll find me: and other stories": Book("Where You'll Find Me: And Other Stories", "Ann Beattie", "074322678X", 5)  
        }


#printing all of the books in the books list
    def display_books(self):    
        for title in sorted(self.books.keys()):
            book = self.books(title)
            print(
                f"Title: {book.title}, "
                f"Author: {book.author}, "
                f"ISBN: {book.ISBN}, "
                f"Quantity: {book.quantity}"
            ) #prints 

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
        for book in user.borrowed_books: #the library loops through the user's borrowed books
            user.return_book(book) #calls the method
            book.update_quantity(1) #updates the book list by adding one
            print(f"{title} has been successfully returned to the library.") #prints a message stating that the book has been returned to the library
            return #stops the function
        
        print("User has not borrowed this book.") #if the book cannot be found, print this message



library = Library() #creating the library object from the library class
library.display_books() #calling the displaying of the books