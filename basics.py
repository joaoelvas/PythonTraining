print(20 * "=")
print("FIRST RUN")
print(20 * "=")

print("Hello, World!")
print("This is my first python program!")

#This is a comment

hello = "Hello, World!" # This is a var

print(hello)

print(20 * "=")
print("LISTS")
print(20 * "=")

# Lists
my_list = ["red","green","blue"]
my_list.append("orange") # add one element to the end of the list
my_list.extend(["black", "white"]) # adds all elements to the end of the list

print(my_list[-1]) # prints the last element of the list
print(my_list[0]) # prints the first element on the list

print(20 * "=")
print("CONDITIONS")
print(20 * "=")

# Conditions # Operators: (==,!=,<,>,<=,>=,not)

if "red" in my_list:
	print("Red is on the list!")
elif "green" in my_list:
	print("Red is not but green is!")
else:
	print("Red and green is not on the list!")

print(20 * "=")
print("LOOPS")
print(20 * "=")

# Loops
for color in my_list:
	print(color)
	print(color.upper()) # .upper() puts in upperCase

start = 10
while start:
	print(start)
	start -= 1
	if start == 5:
		break # break breaks the loop, continue skips the current

print(20 * "=")
print("DELETE")
print(20 * "=")

# Delete
del my_list[0] # Deletes the object at index [0]

print(20 * "=")
print("PROMPTS")
print(20 * "=")

# Prompts

age = input("How old are you? ")
print("Oh you are {}? That is cool!".format(age))


print(20 * "=")
print("FUNCTIONS")
print(20 * "=")

# Functions

def hows_the_parrot():
	print("He's pining fot the pjords!")

def say_hello_to(name):
	if name.lower() == "john":
		print("Hello my master!")
	else:
		print("Hello {}".format(name))

hows_the_parrot()

say_hello_to("John")
say_hello_to("Jenny")

def average(num1,num2):
	return (num1 + num2) / 2

average_num = average(10,20)
print("The average(10,20) is " + str(average_num))


print(20 * "=")
print("EXCEPTIONS")
print(20 * "=")

# Exceptions

try:
	count = int(input("Give me a number: "))
except ValueError:
	print("That's not a number! So a exception was raised!")
else:
	print("Hi " + count)







