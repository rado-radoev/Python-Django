class Book():

    def __init__(self,title,author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return 'Book(Title: {}, Author: {}, Pages: {})'.format(
        self.title, self.author, self.pages
        )

b = Book("Python", "Rado", 1)
print(b)
