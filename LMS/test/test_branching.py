from books.book import Book
from services.borrow_service import BorrowService
from services.search_service import SearchService
from members.member import Member


class SimpleBook(Book):
    def display_book_type(self):
        return "Simple"


def test_member_increments_even_if_book_unavailable(capsys):
    # book already borrowed (unavailable)
    book = SimpleBook(20, "Unavailable", "X", "isbn-u")
    book.set_status(False)
    bs = BorrowService(book)
    member = Member(10, "Edge")

    member.borrow(bs)

    # current implementation increments count regardless of availability
    assert member.get_borrowed_count() == 1
    out = capsys.readouterr().out
    assert "is not available" in out


def test_borrow_service_does_not_change_status_when_unavailable(capsys):
    book = SimpleBook(21, "AlreadyBorrowed", "Y", "isbn-y")
    book.set_status(False)
    bs = BorrowService(book)

    bs.borrow_book()
    out = capsys.readouterr().out
    assert "is not available" in out
    assert book.is_available() is False


def test_search_whitespace_and_case_branches(capsys):
    b1 = SimpleBook(22, "FindMe", "Z", "isbn-22")
    svc = SearchService([b1])

    svc.search_by_title("findme")
    out = capsys.readouterr().out
    assert "Book Found:" in out

    svc.search_by_title(" FindMe ")
    out = capsys.readouterr().out
    # leading/trailing whitespace won't match equality -> not found branch
    assert "Book not found" in out


def test_multiple_borrow_return_sequence(capsys):
    book = SimpleBook(23, "Seq", "A", "isbn-s")
    bs = BorrowService(book)

    # borrow -> unavailable
    bs.borrow_book()
    assert book.is_available() is False

    # return -> available
    bs.return_book()
    assert book.is_available() is True

    # borrow again
    bs.borrow_book()
    assert book.is_available() is False

    out = capsys.readouterr().out
    assert out.count("borrowed successfully") == 2
    


def test_return_when_none_borrowed_decrements_below_zero(capsys):
    book = SimpleBook(24, "NoneBorrowed", "B", "isbn-n")
    bs = BorrowService(book)
    member = Member(20, "Returner")

    # initial count 0, calling return_book will decrement to -1 per current impl
    member.return_book(bs)
    assert member.get_borrowed_count() == -1
    out = capsys.readouterr().out
    assert "returned successfully" in out

def test_return_even_after_multiple_returns(capsys):
    book = SimpleBook(24, "NoneBorrowed", "B", "isbn-n")
    bs = BorrowService(book)
    member = Member(30, "MultiReturner")
    member1= Member(31, "MultiReturner2")

    # borrow once
    member.borrow(bs)
    assert member.get_borrowed_count() == 1

    member1.borrow(bs)
    assert member1.get_borrowed_count() == 1

    # return twice
    member.return_book(bs)
    member.return_book(bs)
    assert member.get_borrowed_count() == -1  # count goes negative
    out = capsys.readouterr().out
    assert "returned successfully" in out
