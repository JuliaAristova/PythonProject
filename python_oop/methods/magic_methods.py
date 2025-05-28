'''
Magic methods - Dunder methods (double underscore) __init__, __str__, __eq__
    They are automatically called by many of Python's built-in operations
    They allow developers to define or customixe the behavior of objects
'''

class Student:

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __str__(self):
        return f"Name: {self.name}; gpa: {self.gpa}"

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.gpa > other.gpa

    def __lt__(self, other):
        return self.gpa < other.gpa

student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.0)

print(student1)
print(student1 == student2)
print(student1 > student2)

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}, number of pages: {self.num_pages}"

    def __eq__(self, other):
        return self.title == other.title and self.author == self.author

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        elif key == 'num_pages':
            return self.num_pages
        else:
            return f"key '{key}' was not found"

book1 = Book("War and Peace", "Leo Tolstoi", 1000)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 300)
book3 = Book("Harry Potter and The Pholosopher's Stone", "J.K.Rowling", 223)
book4 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)
book5 = Book("War and Peace", "Leo Tolstoi", 750)

print(book1)
print(book2)
print(book3)
print(book4)

print(book1 == book5)
print(book4 == book3)
print(book2 > book3)
print(book2 < book3)
print(book4 > book3)
print(book4 < book3)

print(book1 + book2)
print("Lion" in book4)
print("Leo" in book1)

print(book2['title'])
print(book3['author'])
print(book4['num_pages'])
print(book5['is_available'])