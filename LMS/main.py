from books.ebook import Ebook
from books.audiobook import AudioBook
from books.physical_book import PhysicalBook

from library.library import Library

from members.member import Member
from members.faculty import Faculty

from services.borrow_service import BorrowService
from services.search_service import SearchService


# Create Library
library = Library()

# Create Books
ebook = Ebook(
    1,
    "Java Basics",
    "James Gosling",
    "ISBN101",
    5.5
)

audio = AudioBook(
    2,
    "Python Guide",
    "Guido",
    "ISBN102",
    120
)

physical = PhysicalBook(
    3,
    "C++ Programming",
    "Bjarne",
    "ISBN103",
    12
)

# Add Books
library.add_book(ebook)
library.add_book(audio)
library.add_book(physical)

# Create Members
member = Member(
    101,
    "Rahul"
)

faculty = Faculty(
    201,
    "Professor Sharma"
)

# Add Members
library.add_member(member)
library.add_member(faculty)

# Create Borrow Services
ebook_service = BorrowService(ebook)

audio_service = BorrowService(audio)

# Borrow Books
member.borrow(ebook_service)

faculty.borrow(audio_service)

# Search Books
search_service = SearchService(library.books)
search_service.search_by_title("Java Basics")


# Return Book
member.return_book(ebook_service)