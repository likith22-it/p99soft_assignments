from interfaces.searchable import Searchable


class SearchService(Searchable):

    def __init__(self, books):

        self.books = books

    def search_by_title(self, title):

        found = False

        for book in self.books:

            if book.get_title().lower() == title.lower():

                print(
                    "Book Found:",
                    book.get_title()
                )

                found = True

        if not found:

            print("Book not found")

    def search_by_author(self, author):

        found = False

        for book in self.books:

            if book.get_author().lower() == author.lower():

                print(
                    "Book Found:",
                    book.get_title()
                )

                found = True

        if not found:

            print("Book not found")