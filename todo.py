# When 'done' the program quits and shows the list

# list
todo_list = [] 

# add an item to the list
def add_to_list(todo):
	todo_list.append(todo)

# show items on the list
def show_list():
	for todo in todo_list:
		print(todo)

# first input
to_add = input("Add to list: ")

# program loop
while 1:
	if to_add.upper() == "SHOW":
		show_list()
	elif to_add.upper() == "HELP":
		print("DONE to quit")
		print("SHOW to show list")
		print("HELP to ask for help")
	else:
		add_to_list(to_add)
	to_add = input("What next? ")
	if to_add.upper() == "DONE":
		break

# before quit shows all elements of the list
print("Here is your list: ")
show_list()