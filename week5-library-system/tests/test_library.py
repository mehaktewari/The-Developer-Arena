from library_system.library import Library
from library_system.book import Book
from library_system.member import Member

def test_borrow():
    lib = Library()
    lib.add_book(Book("Python", "Guido", "1"))
    lib.add_member(Member("Alex", "M1"))
    assert "Due date" in lib.borrow_book("1", "M1")
