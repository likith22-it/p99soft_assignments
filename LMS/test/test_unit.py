from books.book import Book
from services.borrow_service import BorrowService
from services.search_service import SearchService
from members.member import Member
from members.faculty import Faculty
from library.library import Library


class SimpleBook(Book):
    def display_book_type(self):
        return "Simple"


def test_library_initial_state():
    lib = Library()
    assert isinstance(lib.books, list) and isinstance(lib.members, list)
    assert len(lib.books) == 0 and len(lib.members) == 0


def test_borrowservice_initial_assignment():
    b = SimpleBook(11, "Init", "I", "isbn-i")
    bs = BorrowService(b)
    assert bs.book is b


def test_member_name_and_initial_count():
    m = Member(4, "NameTest")
    assert m.get_name() == "NameTest"
    assert m.get_borrowed_count() == 0


def test_faculty_max_limit_value():
    f = Faculty(5, "ProfTest")
    assert getattr(f, "_max_limit", None) == 5


def test_search_case_insensitive(capsys):
    b1 = SimpleBook(12, "CaseTest", "AuthorX", "isbn-x")
    svc = SearchService([b1])
    svc.search_by_title("casetest")
    out = capsys.readouterr().out
    assert "Book Found:" in out
