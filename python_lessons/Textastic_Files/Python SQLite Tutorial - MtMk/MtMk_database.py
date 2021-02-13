import sqlite3

CREATE_TABLE_BUYING = ("""CREATE TABLE IF NOT EXISTS buying (
			id INTEGER PRIMARY KEY,
			b_date TEXT,
			company TEXT,
			categorie TEXT,
			price INTEGER
			);""")

CREATE_TABLE_BEANS = ("""CREATE TABLE IF NOT EXISTS beans (
			id INTEGER PRIMARY KEY, 
			name TEXT, 
			method TEXT, 
			rating INTEGER
			);""")

CREATE_TABLE_ADDRESSES = ("""CREATE TABLE IF NOT EXISTS addresses (
			id INTEGER PRIMARY KEY,
			first_name TEXT,
			last_name TEXT,
			address TEXT,
			city TEXT,
			zipcode INTEGER,
			country TEXT
			);""")

SQLITE_MASTER_TABLE = 'SELECT name from sqlite_master where type= "table"'

INSERT_NEW_BUYING = "INSERT INTO buying (b_date, company, categorie, price) VALUES (?, ?, ?);"


def connect():
    return sqlite3.connect("buying.db")


def create_tables(connection):
    with connection:
        connection.execute(CREATE_TABLE_BUYING)
        connection.execute(CREATE_TABLE_BEANS)
        connection.execute(CREATE_TABLE_ADDRESSES)

def count_tables(connection):
	with connection:
		return connection.execute(SQLITE_MASTER_TABLE).fetchall()