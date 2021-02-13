from tkinter import*
import MtMk_database

root = Tk()
root.title('Markus Martin - 2020')
root.geometry("500x300")

#myDatabaseConnection = MtMk_database.connect()

'''def count_tables(connection):
	myCursor = connection.cursor()
	myCursor.execute
'''
def exit_form():
    quit()


def newDatabase():
    myDatabaseConnection = MtMk_database.connect()
    MtMk_database.create_tables(myDatabaseConnection)
    print("Database 'buying.db' is created!!!")


def newRecord():
    exit_form()


newDatabase_btn = Button(root, text="Neue Datenbank", command=newDatabase)
exit_btn = Button(root, text="Exit Form!", command=exit_form)
newRecord_btn = Button(root, text="Neuen Datensatz anlegen", command=newRecord)

l_date = Label(root, text="Datum")
l_company = Label(root, text="Geschaeft")
l_categorie = Label(root, text="Kategorie")
l_price = Label(root, text="Preis")

e_date = Entry(root, width=30)
e_company = Entry(root, width=30)
e_categorie = Entry(root, width=30)
e_price = Entry(root, width=30)

newDatabase_btn.grid(row=0, column=1, columnspan=1, pady=0, padx=0, ipadx=30)
exit_btn.grid(row=0, column=0, columnspan=1, pady=10, padx=10, ipadx=30)
newRecord_btn.grid(row=5, column=1, ipadx=30)

l_date.grid(row=1, column=0)
l_company.grid(row=2, column=0)
l_categorie.grid(row=3, column=0)
l_price.grid(row=4, column=0)

e_date.grid(row=1, column=1)
e_company.grid(row=2, column=1)
e_categorie.grid(row=3, column=1)
e_price.grid(row=4, column=1)

root.mainloop()
