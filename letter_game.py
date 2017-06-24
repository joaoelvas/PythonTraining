import os
import random

# LETTER GUESS GAME

# make a list of words
# pick a random word
# draw spaces
# take a guess
# draw guessed letters and strikes
# print out win/loose

words_list = ["facebook", "microsof", "apple", "google", "cisco"]

def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')



def game(w):
	guess_number = 0

	random_index = random.randint(0,len(w) - 1)

	word = w[random_index]

	guessed = ""

	used_letters = ""

	for x in word:
		guessed += "_"

	print(20 * "=")
	print("LET'S START!")
	print(20 * "=")	

	while 1:
		if(guess_number < 10):
			print(20 * "=")
			print("State: " + guessed)
			print("Used letters: " + used_letters)

			guess = input("Take a guess > ")

			guess_number += 1

			if len(guess) > 1:
				print("Thas is not a char, you loose one guess!")
			elif guess in used_letters:
				print("Already used, you loose one guess!")
			else:
				used_letters = used_letters + " " + guess
				if guess in word:
					print("I got one!")
					i = 0
					s = list(guessed)
					while i < len(word):
						if(word[i] == guess):
							s[i] = guess

						i += 1

					guessed = "".join(s)

					if "_" not in guessed:
						print("You got the word: " + word)
						print("You won!")
						break

				else:
					print("That one is not in the word!")

			
		else:
			print("Number of guesses exceded!")
			print("You loose!")
			break

	again = input("Want to play again? (y/n) >")
	if(again == "y"):
		game(w)



game(words_list)










