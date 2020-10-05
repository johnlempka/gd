from flask import Flask, request, g, jsonify
import sqlite3
from book_store import BookStore

app = Flask(__name__)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

store = BookStore()

@app.route('/request', methods=['post'])
def add_book():
    if 'email' not in request.form:
        return "Email is required", 400
    if 'title' not in request.form:
        return "Title is required", 400
    id = store.insert(request.form['email'], request.form['title'])
    if id:
        return get_book(id)

@app.route("/request", methods=['get'])
def list_books():
    books = store.list()
    return jsonify(list(books))

@app.route('/request/<id>', methods=['get'])
def get_book(id):
    book = store.get(id)
    if book:
        return jsonify(book)
    else:
        return "Book not found", 404

@app.route('/request/<id>', methods=['delete'])
def delete_book(id):
    store.delete(id)
    return ''
