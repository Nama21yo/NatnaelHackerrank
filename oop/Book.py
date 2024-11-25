class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    def show_details(self):
        print(f"The book '{self.title}' is written by {self.author} and is priced at ${self.price}.")
# Creating a book object
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99)

# Showing details of the book
book1.show_details()
