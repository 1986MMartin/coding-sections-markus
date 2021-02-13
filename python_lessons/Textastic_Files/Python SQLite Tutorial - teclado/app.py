import database

MENU_PROMPT = """-- Coffee Bean App --

Please chose one of these options:

1) Add new bean.
2) See all beans.
3) Find a bean by name.
4) See wich preparation method is best for a bean.
5) Exit
6) Test_String_Case


Your selection:"""

def menu():
	connection = database.connect()
	database.create_tables(connection)
	
	while (user_input := input(MENU_PROMPT)) != "5":
		if user_input == "1":
			prompt_add_new_bean(connection)
		elif user_input == "2":
			prompt_see_all_beans(connection)
		elif user_input == "3":
			prompt_find_bean(connection)
		elif user_input == "4":
			prompt_find_best_method(connection)
		elif user_input == "6":
			mtmk_String_Case_Test()
		else:
			print("Invalid input, please try again!")

def prompt_add_new_bean(connection):
	name = input("Enter bean name: ")
	method = input("Enter how you've prepared it: ")
	rating = int(input("Enter your rating score (0-100): "))
	database.add_bean(connection, name, method, rating)

def prompt_see_all_beans(connection):
	beans = database.get_all_beans(connection)
	
	for bean in beans:
		print(f"{bean[1]} ({bean[2]}) - {bean[3]}/100")

def prompt_find_bean(connection):
	name = input("Enter bean name to find: ")
	beans = database.get_beans_by_name(connection, name)
	for bean in beans:
		print(f"{bean[1]} ({bean[2]}) - {bean[3]}/100")

def prompt_find_best_method(connection):
	name = input("Enter bean name to find: ")
	best_method = database.get_best_preparation_for_bean(connection, name)
	print(f"The best preparation method for {name} is: {best_method[2]}")

def mtmk_String_Case_Test():
	#name = str(input("Enter a Text: "))
	print("SELECT * FROM beans WHERE name LIKE '%Pink'")
menu()
