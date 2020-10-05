import sqlite3
from flask import g
from datetime import datetime
from constants import DB_LOCATION

def book_from_row(row):
    return  {
        "id": row[0],
        "title": row[1],
        "available": True if row[2] else False,
        "timestamp": row[3]
    }

class BookStore:
    def __init__(self, db=None):
        if db:
            self.db = db
        else:
            self.db = DB_LOCATION

    def get_db(self):
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = sqlite3.connect(self.db)
        return db


    def insert(self, email, title):
        db = self.get_db()
        db.execute('''
            INSERT into "book" (
                "title",
                "timestamp"
            ) VALUES (
                ?,
                ?
            );
        ''', (title,datetime.utcnow(),))
        db.commit()
        raw_id = db.execute('select last_insert_rowid()').fetchone()
        if raw_id:
            return raw_id[0]


    def get(self, id):
        db = self.get_db()
        row = db.execute('''
            SELECT
                "id", "title", "available", "timestamp"
            FROM
                "book"
            WHERE
                "id" = ?
        ''', (id,))
        raw = row.fetchone()
        if raw:
            return book_from_row(raw)

    def list(self):
        db = self.get_db()
        rows = db.execute('''
            SELECT
                "id", "title", "available", "timestamp"
            FROM
                "book"
        ''')
        for row in rows:
            # yield
            yield book_from_row(row)

    def delete(self, id):
        db = self.get_db()
        db.execute('''
            DELETE
            FROM "book"
            WHERE "id" = ?
        ''', (id,))
        db.commit()
