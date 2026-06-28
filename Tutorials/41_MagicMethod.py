# Magic methods (Dunder methods) = special methods with double underscores
# Python calls them automatically behind the scenes when you use operators or built-ins
# __init__, __str__, __eq__ etc — you define them, Python decides when to call them

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        # called automatically when you print(object) or str(object)
        # without this, print(book1) would show something like <__main__.Book object at 0x000001>
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        # similar to __str__ but meant for developers, not end users
        # shown in the console when you type the object name without print()
        # if __str__ is missing, Python falls back to __repr__
        return f"Book({self.title}, {self.author}, {self.num_pages})"

    def __eq__(self, other):
        # called when you use == between two objects
        # by default == checks if both variables point to the same object in memory
        # overriding it lets you define what "equal" actually means for your class
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        # called when you use < (less than)
        # here we compare by page count
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        # called when you use > (greater than)
        return self.num_pages > other.num_pages

    def __le__(self, other):
        # called when you use <= (less than or equal)
        return self.num_pages <= other.num_pages

    def __ge__(self, other):
        # called when you use >= (greater than or equal)
        return self.num_pages >= other.num_pages

    def __add__(self, other):
        # called when you use + between two objects
        # here we add page counts together
        return f"{self.num_pages + other.num_pages} pages"

    def __contains__(self, keyword):
        # called when you use 'in' keyword
        # e.g. "Lion" in book3 checks if "Lion" appears in title or author name
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        # called when you use square bracket access like book["title"]
        # lets objects behave like dictionaries for key based access
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found"

    def __len__(self):
        # called when you use len(object)
        # here we return page count as the "length" of a book
        return self.num_pages

    def __del__(self):
        # called when the object is about to be destroyed / garbage collected
        # useful for cleanup like closing files or database connections
        print(f"'{self.title}' has been deleted from memory")


book1 = Book("HowToStayJobless", "Tawsif Azam", 310)
book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)

print(book1)              # calls __str__        -> 'HowToStayJobless' by Tawsif Azam
print(repr(book1))        # calls __repr__       -> Book(HowToStayJobless, Tawsif Azam, 310)

print(book1 == book3)     # calls __eq__         -> False (different title and author)
print(book1 == Book("HowToStayJobless", "Tawsif Azam", 999))  # True (same title and author, pages ignored)

print(book1 < book2)      # calls __lt__         -> False (310 is not less than 223)
print(book2 > book3)      # calls __gt__         -> True  (223 > 172)
print(book3 <= book2)     # calls __le__         -> True  (172 <= 223)
print(book1 >= book2)     # calls __ge__         -> True  (310 >= 223)

print(book1 + book2)      # calls __add__        -> 533 pages

print("Lion" in book3)    # calls __contains__   -> True  ("Lion" is in the title)
print("Tolkien" in book1) # calls __contains__   -> True  ("Tolkien" is in the author)
print("Rowling" in book3) # calls __contains__   -> False

print(book3["title"])     # calls __getitem__    -> The Lion, the Witch and the Wardrobe
print(book1["author"])    # calls __getitem__    -> Tawsif Azam
print(book2["num_pages"]) # calls __getitem__    -> 223
print(book1["price"])     # calls __getitem__    -> Key 'price' was not found

print(len(book1))         # calls __len__        -> 310
print(len(book3))         # calls __len__        -> 172

# __del__ fires when object is deleted or goes out of scope
del book3                 # calls __del__        -> 'The Lion, the Witch and the Wardrobe' has been deleted from memory