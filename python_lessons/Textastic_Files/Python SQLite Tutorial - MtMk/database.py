import sqlite3

CREATE_TABLE_TRADE = ("""CREATE TABLE IF NOT EXISTS trade (
	);""")


def connect():
    return sqlite3.connect("trade.db")


def create_tables(connection):
    with connection:
        connection.execute(CREATE_TABLE_TRADE)
