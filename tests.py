import unittest
from init_db import init, drop
from flask import Flask
from book_store import BookStore

DB_LOCATION = "test.db"

app = Flask(__name__)

class TestBookStore(unittest.TestCase):
    def setUp(self):
        init(DB_LOCATION)
        self.store = BookStore(DB_LOCATION)

    def test_insert_delete(self):
        with app.app_context():
            self.store.insert("johnlempka@gmail.com", "test 1")
            self.store.insert("johnlempka@gmail.com", "test 2")

            books = self.store.list()

            self.assertEqual(2, len(list(books)))

            self.store.delete(1)

            books = self.store.list()

            self.assertEqual(1, len(list(books)))

    def test_book_not_found(self):
        with app.app_context():
            book = self.store.get(2244)
            self.assertEqual(None, book)

    def tearDown(self):
        drop(DB_LOCATION)

if __name__ == '__main__':
    unittest.main()
