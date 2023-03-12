# Q4: Create a class Book with two attributes title and author. The class
# should have a method display() that prints the title and author of the
# book.


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        return print(f"Title:\t{self.title}\nAuthor:\t{self.author}")


b1 = Book("Until I Say Goodbye", "Susan Spencer")
b1.display()
