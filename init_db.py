import sqlite3
from constants import DB_LOCATION

def init(db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    sql_file = open("schema.sql")
    sql_as_string = sql_file.read()
    cursor.executescript(sql_as_string)

def drop(db):
    import os
    os.remove(db)

def main():
    init(DB_LOCATION)


if __name__ == '__main__':
    main()
