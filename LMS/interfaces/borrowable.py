from abc import ABC, abstractmethod


class Borrowable(ABC):

    @abstractmethod
    def borrow_book(self):
        pass

    @abstractmethod
    def return_book(self):
        pass