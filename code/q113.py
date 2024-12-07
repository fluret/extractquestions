### code départ
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"{self.name}, {self.age} years old, {self.gender}"

# Create an instance of the Person class
person1 = Person("Juan", 25, "Male")

# Print the information of the person using the __str__ method
print(person1)  # Output: Juan, 25 years old, Male
### correction
# Your code here

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Book Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}"

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

print(book1)
### test.py
import pytest
from app import Book

@pytest.mark.it("The Book class exists")
def test_book_class_exists():
    try:
        assert Book
    except AttributeError:
        raise AttributeError("The class 'Book' should exist in app.py")

@pytest.mark.it("The Book class has the __init__ method")
def test_book_has_init_method():
    assert hasattr(Book, "__init__")

@pytest.mark.it("The __init__ method initializes the title, author, and year attributes")
def test_init_method_initializes_attributes():
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    assert hasattr(book, "title")
    assert hasattr(book, "author")
    assert hasattr(book, "year")

@pytest.mark.it("The Book class has the __str__ method")
def test_book_has_str_method():
    assert hasattr(Book, "__str__")

@pytest.mark.it("The __str__ method returns the expected string")
def test_str_method_returns_expected_string(capsys):
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    print(book)
    captured = capsys.readouterr()
    expected_output = "Book Title: The Great Gatsby\nAuthor: F. Scott Fitzgerald\nYear: 1925\n"
    assert captured.out == expected_output