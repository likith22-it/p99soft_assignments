from abc import ABC, abstractmethod


class Searchable(ABC):

    @abstractmethod
    def search_by_title(self, title):
        pass

    @abstractmethod
    def search_by_author(self, author):
        pass