from books.book import Book
from services.borrow_service import BorrowService
from services.search_service import SearchService
from members.member import Member
from members.faculty import Faculty


class SimpleBook(Book):
    def display_book_type(self):
        return "Simple"


def test_borrow_service_borrow_and_return(capsys):
    book = SimpleBook(5, "Borrowable", "Dan", "isbn-b")
    bs = BorrowService(book)

    assert book.is_available() is True
    bs.borrow_book()
    out = capsys.readouterr().out
    assert "borrowed successfully" in out
    assert book.is_available() is False

    # try borrowing when not available
    bs.borrow_book()
    out = capsys.readouterr().out
    assert "is not available" in out

    bs.return_book()
    out = capsys.readouterr().out
    assert "returned successfully" in out
    assert book.is_available() is True


def test_member_borrow_and_return_counts(capsys):
    book = SimpleBook(6, "Countable", "Eve", "isbn-c")
    bs = BorrowService(book)
    member = Member(1, "Member One")

    assert member.get_borrowed_count() == 0

    member.borrow(bs)
    assert member.get_borrowed_count() == 1

    member.borrow(bs)
    assert member.get_borrowed_count() == 2

    # exceed default limit (2)
    member.borrow(bs)
    out = capsys.readouterr().out
    assert "Borrow limit reached" in out
    assert member.get_borrowed_count() == 2

    # return reduces count
    member.return_book(bs)
    assert member.get_borrowed_count() == 1


def test_faculty_max_limit(capsys):
    book = SimpleBook(7, "FacultyBook", "Frank", "isbn-f")
    bs = BorrowService(book)
    faculty = Faculty(2, "Prof")

    for _ in range(5):
        faculty.borrow(bs)

    assert faculty.get_borrowed_count() == 5

    # one more should hit limit
    faculty.borrow(bs)
    out = capsys.readouterr().out
    assert "Borrow limit reached" in out
    assert faculty.get_borrowed_count() == 5


def test_search_service_title_and_author(capsys):
    b1 = SimpleBook(8, "FindMe", "Gina", "isbn-1")
    b2 = SimpleBook(9, "Other", "Gina", "isbn-2")
    svc = SearchService([b1, b2])

    svc.search_by_title("FindMe")
    out = capsys.readouterr().out
    assert "Book Found:" in out and "FindMe" in out

    svc.search_by_author("Gina")
    out = capsys.readouterr().out
    assert out.count("Book Found:") >= 1

    svc.search_by_title("Nope")
    out = capsys.readouterr().out
    assert "Book not found" in out
