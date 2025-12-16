from library_system.book import Book
from library_system.member import Member

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.isbn] = book

    def add_member(self, member):
        self.members[member.member_id] = member

    def borrow_book(self, isbn, member_id):
        if isbn not in self.books:
            return "Book not found"
        if member_id not in self.members:
            return "Member not found"

        book = self.books[isbn]
        member = self.members[member_id]

        if not member.can_borrow():
            return "Borrow limit reached"

        success, msg = book.check_out(member_id)
        if success:
            member.borrow_book(isbn)
        return msg

    def return_book(self, isbn, member_id):
        if isbn in self.books and member_id in self.members:
            self.books[isbn].return_book()
            self.members[member_id].return_book(isbn)
            return "Book returned successfully"
        return "Invalid return"

    def search_books(self, keyword):
        keyword = keyword.lower()
        return [b for b in self.books.values()
                if keyword in b.title.lower()
                or keyword in b.author.lower()
                or keyword in b.isbn]
