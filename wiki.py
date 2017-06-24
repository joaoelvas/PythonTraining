import datetime

answer_format = '%m/%d'
link_format = '%b_%d'

link = 'https://en.wikipedia.org/wiki/{}'

while 1:
	answer = input("What date would you like? Plese use the MM/DD format. Enter 'quit' to quit. ")

	if answer.upper() == 'QUIT':
		break

	try:
		date = datetime.datetime.strptime(answer,aswer_format)
		output = link.format(date.strftime(link_format))
		print(output)
	except ValueError:
		print("That's not a valid date. Please try again.")