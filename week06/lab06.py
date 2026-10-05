"""Classes for representing printed books and electronic books."""

from datetime import date


class Book:
    """Represent a book with its title, author, and publication year."""

    def __init__(self, title, author, year):
        """Store the book's title, author, and publication year."""
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """Return the book's title, author, and publication year."""
        return f"{self.title} by {self.author} ({self.year})"

    def get_age(self):
        """Return the number of years since publication."""
        return date.today().year - self.year


class EBook(Book):
    """Represent an electronic book with a file size in megabytes."""

    def __init__(self, title, author, year, file_size):
        """Store the book details and its electronic file size."""
        super().__init__(title, author, year)
        self.file_size = file_size

    def __str__(self):
        """Return the book details and file size in megabytes."""
        return f"{super().__str__()} - {self.file_size} MB"
