from interfaces.borrowable import Borrowable


class BorrowService(Borrowable):

    def __init__(self, book):

        self.book = book

    def borrow_book(self):

        if self.book.is_available():

            self.book.set_status(False)

            print(
                self.book.get_title(),
                "borrowed successfully"
            )

        else:

            print(
                self.book.get_title(),
                "is not available"
            )

    def return_book(self):

        self.book.set_status(True)

        print(
            self.book.get_title(),
            "returned successfully"
        )