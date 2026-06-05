from books.book import Book


class Ebook(Book):

    def __init__(self,
                 book_id,
                 title,
                 author,
                 isbn,
                 file_size):

        super().__init__(
            book_id,
            title,
            author,
            isbn
        )

        self.__file_size = file_size

    def get_file_size(self):
        return self.__file_size

    def display_book_type(self):
        print("This is an Ebook")