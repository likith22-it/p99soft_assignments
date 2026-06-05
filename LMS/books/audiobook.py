from books.book import Book


class AudioBook(Book):

    def __init__(self,
                 book_id,
                 title,
                 author,
                 isbn,
                 duration):

        super().__init__(
            book_id,
            title,
            author,
            isbn
        )

        self.__duration = duration

    def get_duration(self):
        return self.__duration

    def display_book_type(self):
        print("This is an AudioBook")