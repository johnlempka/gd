import sqlite3
from constants import DB_LOCATION
from datetime import datetime

def main():
    conn = sqlite3.connect(DB_LOCATION)
    cursor = conn.cursor()

    books = [
        ("For Whom The Bell Tolls", datetime.utcnow(), True),
        ("The Sun Also Rises", datetime.utcnow(), True),
        ("Those Who Leave And Those Who Stay",  datetime.utcnow(), False)
    ]

    cursor.executemany('INSERT INTO "book" ("title", "timestamp", "available") VALUES (?,?,?)', books)
    conn.commit()

if __name__ == '__main__':
    main()
