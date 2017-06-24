todo_list = []

def show_help():
	print("\n1. Separate each item with a comma.")
	print("2. Type DONE to quit;\n3. SHOW to see the current list;\n4. HELP to see available commands")

show_help()

def show_list():
	count = 1
	for item in todo_list:
		print("{}: {}".format(count,item))
		count += 1

def add_to_list(item):
	todo_list.append(item)

def add_to_list_at_index(index, item):
	todo_list.insert(index,item)

def remove_from_list(index):
	todo_list.remove(todo_list[index - 1])

while 1:
	new_item = input("> ")

	if new_item == "DONE":
		print("\n Here is your list:")
		show_list()
		break
	elif new_item == "HELP":
		show_help()
		continue
	elif new_item == "SHOW":
		show_list()
		continue
	elif new_item == "REMOVE":
		rem = input("What item do you want to remove? (number on the list) > ")
		remove_from_list(rem - 1)
	else:
		new_list = new_item.split(",")
		index = input("Add this at a certain spot? Press enter for the end of the list, "
					  "or give me a number. Currently {} items on the list. > ".format(len(todo_list)))

		if index:
			print(new_list)
			spot = int(index) - 1
			for item in new_list:
				add_to_list_at_index(spot,item.strip())
				# strip cuts space at the beggining and at the end
				spot += 1
		else:
			for item in new_list:
				add_to_list(item.strip())



