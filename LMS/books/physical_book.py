from books.book import Book


class PhysicalBook(Book):

    def __init__(self,
                 book_id,
                 title,
                 author,
                 isbn,
                 shelf_number):

        super().__init__(
            book_id,
            title,
            author,
            isbn
        )

        self.__shelf_number = shelf_number

    def get_shelf_number(self):
        return self.__shelf_number

    def display_book_type(self):
        print("This is a Physical Book")