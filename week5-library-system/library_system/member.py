class Member:
    def __init__(self, name, member_id):
        self.name = name.title()
        self.member_id = member_id.upper()
        self.borrowed_books = []
        self.max_books = 5

    def can_borrow(self):
        return len(self.borrowed_books) < self.max_books

    def borrow_book(self, isbn):
        self.borrowed_books.append(isbn)

    def return_book(self, isbn):
        if isbn in self.borrowed_books:
            self.borrowed_books.remove(isbn)

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        member = cls(data["name"], data["member_id"])
        member.borrowed_books = data["borrowed_books"]
        return member
