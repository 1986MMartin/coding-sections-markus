from tkinter import*
import sqlite3

root = Tk()
root.title('Markus Martin - 2020')
root.geometry("600x600")

myDatabaseConnection = sqlite3.connect("buying.db")
myDatabaseCursor = myDatabaseConnection.cursor()

CREATE_TABLE_BUYING = ("""CREATE TABLE IF NOT EXISTS buying (
			id INTEGER PRIMARY KEY,
			b_date TEXT,
			company TEXT,
			categorie TEXT,
			price INTEGER
			);""")


def exit_form():
    quit()


def newDatabase():
    myDatabaseConnection = sqlite3.connect('buying.db')
    myDatabaseCursor = myDatabaseConnection.cursor()
    myDatabaseCursor.exectue(("""CREATE TABLE IF NOT EXISTS buying (
				id INTEGER PRIMARY KEY,
				b_date TEXT,
				company TEXT,
				categorie TEXT,
				price INTEGER
				);""")
#    myDatabaseConnection.commit()
#    myDatabaseConnection.close()
    print("Database is created!")

# label, button, entry-fields declaration


newDatabase_btn=Button(root, text="Create new Database", command=newDatabase)
exit_btn=Button(root, text="Exit Form!", command=exit_form)

l_date=Label(root, text="Datum")
l_company=Label(root, text="Geschaeft")
l_categorie=Label(root, text="Kategorie")
l_price=Label(root, text="Preis")

e_date=Entry(root, width=30)
e_company=Entry(root, width=30)
e_categorie=Entry(root, width=30)
e_price=Entry(root, width=30)

newDatabase_btn.grid(row=0, column=1, columnspan=1, pady=0, padx=0, ipadx=30)
exit_btn.grid(row=0, column=0, columnspan=1, pady=10, padx=10, ipadx=20)

l_date.grid(row=1, column=0)
l_company.grid(row=2, column=0)
l_categorie.grid(row=3, column=0)
l_price.grid(row=4, column=0)

e_date.grid(row=1, column=1)
e_company.grid(row=2, column=1)
e_categorie.grid(row=3, column=1)
e_price.grid(row=4, column=1)


root.mainloop()
