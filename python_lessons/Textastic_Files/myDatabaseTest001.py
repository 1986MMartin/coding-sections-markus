import sqlite3
import os
os.system('clear')

conn = sqlite3.connect('customer.db')
c = conn.cursor()

def submit():
	return

def query():
	return

'''
c.execute("""CREATE TABLE customer (
		first_name text,
		last_name text,
		email text
		) """)
'''
# c.execute("INSERT INTO customer VALUES ('Markus','Martin','1986mmartin@gmail.com')")
#print("Daten erfolgreich gespeichert.!")

c.execute("SELECT * FROM customer")
items = c.fetchall()

for item in items:
	print(item[0] + " " + item[1])


conn.commit()
conn.close()