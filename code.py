
#creating the book class which features the title, author and ISBN
class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author

#creating the library class which holds the books
class Library:
    def __init__(self):
        self.books = []

#simple book dataset
books = [
    Book("Classical Mythology", "Mark P. O. Morford", "0195153448"),
    Book("Clara Callan", "Richard Bruce Wright", "0002005018"),
    Book("Decision in Normandy", "Carlo D'Este", "0060973129"),
    Book("Flu: The Story of the Great Influenza Pandemic of 1918 and the Search for the Virus That Caused It", "Gina Bari Kolata", "0374157065"),
    Book("The Mummies of Urumchi", "E. J. W. Barber", "0393045218"),
    Book("The Kitchen God's Wife", "Amy Tan", "0399135782"),
    Book("What If?: The World's Foremost Military Historians Imagine What Might Have Been", "Robert Cowley", "0425176428"),
    Book("PLEADING GUILTY", "Scott Turow", "0671870432"),
    Book("Under the Black Flag: The Romance and the Reality of Life Among the Pirates", "David Cordingly", "0679425608"),
    Book("Where You'll Find Me: And Other Stories", "Ann Beattie", "074322678X")
]

