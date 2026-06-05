from books.ebook import Ebook
from books.audiobook import AudioBook
from books.physical_book import PhysicalBook
from books.book import Book
from library.library import Library
from members.member import Member


class SimpleBook(Book):
    def display_book_type(self):
        return "Simple"


def test_ebook_file_size_and_display(capsys):
    ebook = Ebook(2, "Ebook Title", "Alice", "isbn-ebook", file_size=3.5)
    assert ebook.get_file_size() == 3.5
    ebook.display_book_type()
    captured = capsys.readouterr()
    assert "This is an Ebook" in captured.out


def test_audiobook_duration_and_display(capsys):
    audio = AudioBook(3, "Audio Title", "Bob", "isbn-audio", duration=120)
    assert audio.get_duration() == 120
    audio.display_book_type()
    captured = capsys.readouterr()
    assert "This is an AudioBook" in captured.out


def test_physicalbook_shelf_and_display(capsys):
    phys = PhysicalBook(4, "Phys Title", "Carol", "isbn-phys", shelf_number="A12")
    assert phys.get_shelf_number() == "A12"
    phys.display_book_type()
    captured = capsys.readouterr()
    assert "This is a Physical Book" in captured.out


def test_library_add_book_and_member(capsys):
    lib = Library()
    book = SimpleBook(10, "LibTitle", "Hank", "isbn-lib")
    member = Member(3, "MemberTwo")

    lib.add_book(book)
    out = capsys.readouterr().out
    assert "added to library" in out
    assert book in lib.books

    lib.add_member(member)
    out = capsys.readouterr().out
    assert "added as member" in out
    assert member in lib.members
