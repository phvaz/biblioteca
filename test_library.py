import unittest
from library import Book, Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book('Hamlet', 'Romance', 'Shakespeare', True)
        self.book2 = Book('Harry Potter', 'Fantasy', 'J.K. Rowling', True)

    def test_add_books(self):
        self.library.add_books(self.book1)
        self.library.add_books(self.book2)
        self.assertEqual(len(self.library.shelf), 2)

    def test_remove_book(self):
        self.library.add_books(self.book1)
        self.library.remove_book(self.book1)
        self.assertEqual(len(self.library.shelf), 0)

    def test_search_book_available(self):
        self.library.add_books(self.book1)
        result = self.library.search_book('Hamlet')
        self.assertEqual(result, 'O livro está disponível.')

    def test_search_book_unavailable(self):
        self.library.add_books(self.book1)
        self.book1.availability = False
        result = self.library.search_book('Hamlet')
        self.assertEqual(result, 'Este livro não está disponível.')

if __name__ == '__main__':
    unittest.main()
