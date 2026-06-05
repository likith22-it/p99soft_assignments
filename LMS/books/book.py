from abc import ABC, abstractmethod


class Book(ABC):

    def __init__(self, book_id,
                 title,
                 author,
                 isbn):

        self.__id = book_id
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__status = True

    # Getters
    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_isbn(self):
        return self.__isbn

    def is_available(self):
        return self.__status

    # Setter
    def set_status(self, status):
        self.__status = status

    @abstractmethod
    def display_book_type(self):
        pass