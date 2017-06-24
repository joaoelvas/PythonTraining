import random

# secret number
secret = random.randint(1,10)

# list of all tries
tries = []


# game function
def start_game():
	# reset tries at start
	tries = []
	while len(tries) < 5:
		try:
			guess = int(input("Say a number: "))
		except ValueError:
			print("Not an integer number!")
		else:
			tries.append(guess)
			if guess == secret:
				print("You got it. My number was: {}".format(secret))
				print("You tried {} time/s".format(len(tries)))
				break
			else:
				if guess > secret:
					print("Too high")
				else:
					print("Too low")
	# start again
	start = input("Wanna play again? ")
	if start.lower() == 'yes':
		start_game()
	else:
		print("Bye!")

# initial call
start_game()

# For next exercise try to revert this exercise
# Computer tries to guess the number
