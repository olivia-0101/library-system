
#creating the book class which features the title, author, ISBN and the quantity of the books available
class Book:
    def __init__(self, title, author, ISBN, quantity):
        self.title = title #title of the book
        self.author = author #author of the book
        self.ISBN = ISBN #ISBN of the book
        self.quantity = quantity #quantity of the book available to take out

#creating the library class which holds the books

class Library:
    def __init__(self):
        self.books = []

#if there is an error and there are no books in the library, inform the user and stop the function
    def display_books(self):
        if not self.books:
            print("There are no books.")
            return
        for book in self.books:
            print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}, quantity: {self.quantity}")

library = Library()
    
#simple hard-coded book dataset
library.books = [
    Book("Classical Mythology", "Mark P. O. Morford", "0195153448", "2"),
    Book("Clara Callan", "Richard Bruce Wright", "0002005018", "3"),
    Book("Decision in Normandy", "Carlo D'Este", "0060973129", "4"),
    Book("Flu: The Story of the Great Influenza Pandemic of 1918 and the Search for the Virus That Caused It", "Gina Bari Kolata", "0374157065", "10"),
    Book("The Mummies of Urumchi", "E. J. W. Barber", "0393045218", "9"),
    Book("The Kitchen God's Wife", "Amy Tan", "0399135782", "5"),
    Book("What If?: The World's Foremost Military Historians Imagine What Might Have Been", "Robert Cowley", "0425176428", "8"),
    Book("PLEADING GUILTY", "Scott Turow", "0671870432", "3"),
    Book("Under the Black Flag: The Romance and the Reality of Life Among the Pirates", "David Cordingly", "0679425608", "1"),
    Book("Where You'll Find Me: And Other Stories", "Ann Beattie", "074322678X", "5")
]

library.display_books