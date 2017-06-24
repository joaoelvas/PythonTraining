import re

names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()

# print(re.match(r'Love', data)) # The r before means it is a raw String
# print(re.search(r'Kenneth', data))
# print(re.search(r'\(\d\d\d\) \d\d\d-\d\d\d\d', data))
# print(re.search(r'\(\d{3}\) \d{3}-\d{4}', data)) # same as line above
# print(re.findall(r'\(?\d{3}\)? \d{3}-\d{4}', data)) # the ? after the parenthisis makes them optional
# print(re.search(r'\w+, \w+', data))
# print(re.findall(r'\w+, \w+', data))
# print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))
# print(re.findall(r'\b[trehous]{9}\b', data, re.IGNORECASE))

#print(re.findall(r'''
#	\b@[-\w\d.]*	# First a word boundary, an @, and then any number of character
#	[^gov\t]+	# Ignore 1+ instances of the letters 'g', 'o' or 'v' and a tab
#	\b    # Match another word boundary
#''', data, re.VERBOSE|re.I))

#print(re.findall(r"""
#	\b[-\w]+, # Find a word boundary, 1+ hyphens or characters, and a comma
#	\s # Find one whitespace
#	[-\w ] # 1+ hyphens and characters and explicit spaces
#	[^\t\n] # Ignore tabs and newlines
#""", data, re.X))


#line = re.search(r''' # will print a touple with all of the groups bellow
#	^(?P<name>[-\w ]*,\s[-\w ]+)\t # a group with last and first names
#	(?P<email>[-\w\d.+]+@[-\w\d.]+)\t # a group with email
#	(?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t # a group with Phone
#	(?P<job>[\w\s]+, \s[\w\s.]+)\t? # a group with Job and company
#	(?P<twitter>@[\w\d]+)?$ # a group with Twitter
#''', data, re.X|re.MULTILINE)

line = re.compile(r''' # will print a touple with all of the groups bellow
	^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t # a group with last and first names
	(?P<email>[-\w\d.+]+@[-\w\d.]+)\t # a group with email
	(?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t # a group with Phone
	(?P<job>[\w\s]+, \s[\w\s.]+)\t? # a group with Job and company
	(?P<twitter>@[\w\d]+)?$ # a group with Twitter
''', re.X|re.MULTILINE)

#print(line)
#print(line.groupdict())
#print(re.search(line,data).groupdict())
#print(line.search(data).groupdict())

#for match in line.finditer(data): # everybody's names in .txt file
#	print(match.)

for match in line.finditer(data): # everybody's names in .txt file
	print('{first} {last} <{email}>'.format(**match.groupdict()))