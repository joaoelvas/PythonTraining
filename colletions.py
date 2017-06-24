print(20 * "=")
print("LISTS")
print(20 * "=")

print()

a_list = [1, 2, 3]

a_list.append([4, 5]) # adds a list at last member of the list

print(a_list)

print()
print(20 * "-")
print()

our_list = list(range(10)) # range creates a list from [0,...,9]

our_list = our_list + [10, 11, 12]

print(our_list)

print()
print(20 * "-")
print()

our_list.extend(range(13, 21)) # extends the list

print(our_list)

print()
print(20 * "-")
print()

alpha = list('acdf') # creates a list [a,c,d,f]

print(alpha)

alpha.insert(1,'b') # inserts at index

print(alpha)

alpha.insert(4,'e') # inserts at index

print(alpha)

print()
print(20 * "-")
print()

del alpha[4] # remove at index

print(alpha)

alpha.remove('b') # remove by value, only the first instance

print(alpha)

print()
print(20 * "-")
print()

print(alpha)
item = alpha.pop(0) # pop returns the item that was removed

print(item)
print(alpha)

print()
print(20 * "-")
print()

# SLICES

my_list = list(range(1,6))

print(my_list)

my_s_list = my_list[2:len(my_list)] # [3,4,5]

print(my_s_list)

b_to_x = my_list[:2] # begining util 2

print(b_to_x)

x_to_e = my_list[2:] # 2 until end

print(x_to_e)

my_list_copy = my_list[:] # gets a copy of the list

my_list.sort() # sorts the list

my_list = list(range(20))

my_list_copy = my_list[::2] # jumps index 2 by 2 like my_list[0],my_list[2],my_list[4]

print(my_list_copy)

my_list_copy = my_list[2::2] # starts at index 2 and jumps by 2

print(my_list_copy)

my_list_copy = my_list[::-1] # list backwards

print(my_list_copy)

my_list_copy = my_list[8:2:-1]

print(my_list_copy)

messy_list = [1, 2, 'a', 'b', 'c', 'd', 5, 6, 7, 'f', 'g', 'h', 8, 9, 'j']

# lets now order the list with only letters not numbers

del messy_list[:2]

print(messy_list)

messy_list[4:7] = ['e','f']

print(messy_list)

messy_list.remove('f')

print(messy_list)

messy_list[8:10] = 'i'

print(messy_list)


print(20 * "=")
print("DICTIONARIES")
print(20 * "=")

# Dictionaries

# key : name
# val : Kenneth
my_dict = {'name': 'Kenneth'} 

print(my_dict)

my_dict = {'name': 'Kenneth', 'job': 'Teacher'} 

print(my_dict)

game_dict = {(2,2): True, (1,2): False}

print(game_dict[(1,2)])

print()
print(20 * "-")
print()

# A function named members that takes two arguments, a dictionary 
# and a list of keys. Return a count of how many of the items in 
# the list are also keys in the dictionary.

def members(dict,keys):
	count = 0
	for key in keys:
		if key in dict:
			count += 1
	return count


my_dict = {'apples': 1, 'bananas': 2, 'coconuts': 3}
my_list = ['apples', 'coconuts', 'grapes', 'strawberries']

print(members(my_dict,my_list))

my_dict = {'name': 'Kenneth', 'job': 'Teacher'}

print()
print(my_dict)

del my_dict['job']

print(my_dict)

my_dict['age'] = 34

print(my_dict)

# update with new keys and values
my_dict.update({'job': 'Teacher', 'age': 33, 'state': 'Oregon', 'name': 'Kenneth Love'})

print()
print(my_dict)

print()
print(20 * "-")
print()

my_string = "Hi, my name is {name}, and I live in {state}"

print(my_string.format(**my_dict))

for key in my_dict: #loops over the keys
	print(my_dict[key]) # prints the value of each key

print()

print(20 * "=")
print("TUPLES")
print(20 * "=")

# Tuples

my_tuple = (1,2,3)
my_second_tuple = 1,2,3 # same as (1,2,3)
my_third_tuple = tuple([1,2,3]) # have to pass an iterable

print(my_tuple[1])

print()

a, b = 1, 2
print(a)
print(b)

c = (3,4)

d, e = c

f = d, e

f == c # TRUE

print()
print(20 * "-")
print()

# SWAPING VALUES

a, b = b, a # swaps a with b, and b with a

my_alpha = "abcdefghijklmnopqrstuvxz"

for index,letter in enumerate(my_alpha):
	print("{}: {}".format(index,letter))

print()
print(20 * "-")
print()

for step in enumerate(my_alpha):
	print("{}: {}".format(step[0],step[1]))

print()
print(20 * "-")
print()

for step in enumerate(my_alpha):
	print("{}: {}".format(*step))

print()
print(20 * "-")
print()

for key, value in my_dict.items():
	print('{}: {}'.format(key.title(), value))






def combo(it1, it2):
    new_list = []
    count = 0
    
    while count < len(it1):
        t = it1[count],it2[count]
        new_list.append(t)
        count += 1
                        
    return new_list






