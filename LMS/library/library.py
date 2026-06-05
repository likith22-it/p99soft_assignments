class Library:

    def __init__(self):

        self.books = []
        self.members = []

    def add_book(self, book):

        self.books.append(book)

        print(
            book.get_title(),
            "added to library"
        )

    def add_member(self, member):

        self.members.append(member)

        print(
            member.get_name(),
            "added as member"
        )
        