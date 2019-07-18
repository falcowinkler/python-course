import sqlite3

create_table_statement = """
CREATE TABLE IF NOT EXISTS ufo_sights (
    time string,
    summary string,
    shape string,
    location string
);"""


def create_ufo_table_if_not_exists(conn):
    conn.cursor().execute(create_table_statement)
    conn.commit()


def save_to_database(conn, record):
    conn.cursor().execute("INSERT INTO ufo_sights (time, location, shape, summary) VALUES (?, ?, ?, ?)", record)
    conn.commit()


def open_connection():
    return sqlite3.connect("ufo-db.sqlite")
