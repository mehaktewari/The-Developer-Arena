from library_system.book import Book

def test_book_creation():
    b = Book("Python", "Guido", "123")
    assert b.available is True
