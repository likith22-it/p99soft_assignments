class Member:

    def __init__(self,
                 member_id,
                 name):

        self.__member_id = member_id
        self.__name = name

        self._max_limit = 2
        self.__borrowed_count = 0

    def get_name(self):
        return self.__name

    def get_borrowed_count(self):
        return self.__borrowed_count

    def borrow(self, borrow_service):

        if self.__borrowed_count < self._max_limit:

            borrow_service.borrow_book()

            self.__borrowed_count += 1

        else:

            print("Borrow limit reached")

    def return_book(self, borrow_service):

        borrow_service.return_book()

        self.__borrowed_count -= 1