import sqlite3
import MtMk_database

'''
con = sqlite3.connect('buying.db')

def sql_fetch(con):

    cursorObj = con.cursor()

    cursorObj.execute('SELECT name from sqlite_master where type= "table"')

    print(cursorObj.fetchall())


sql_fetch(con)
'''

myDatabaseConnection = MtMk_database.connect()
count_tables_database = MtMk_database.count_tables(myDatabaseConnection)

for count_table in count_tables_database:
    print(count_table)
