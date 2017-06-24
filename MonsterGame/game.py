import sys

from character import Character
from monster import Dragon
from monster import Goblin
from monster import Troll


class Game:

	# sets the game
	def setup(self):
		self.player = Character()
		self.monsters = [Goblin(), Troll(), Dragon()]
		self.monster = self.get_next_monster()

	# Returns the next monster in the list
	def get_next_monster(self):
		try:
			return self.monsters.pop(0)
		except IndexError:
			return None

	def monster_turn(self):
		# Check to see if the monster attacks
		if self.monster.attack():
			# If so, tell the player
			print("{} attacked!".format(self.monster))
			# Check if the player wants to dodge
			play = input("Do you want to dodge? [y/n] > ")
			if play.upper == 'Y':
				# If so, see if the dodge is successfull
				if self.player.dodge():
					print("Player dodged!")
					# If it is, move on
				# If its not remove 1 HP from player
				else:
					self.player.hit_points -= 1
			else:
				self.player.hit_points -= 1
		# If the monster isn't attacking, tell that to the player too.
		else:
			print("{} attack was not successfull!".format(self.monster))

	def player_turn(self):
		# Let the player attack, rest or quit
		move = input("You can [A]ttack, [R]est or [Q]uit. > ")
		move = move.upper()

		# If he attack's:
		if move == 'A':
			# See if the atack is successfull
			if self.player.attack():
				print("Player is attacking!")
				# If so, see if the monster dodges
				if self.monster.dodge():
					# If dodged print that
					print("{} dodged!".format(self.monster))
				# If not dodged, subtract the right amount of hp from monster
				else:
					if self.player.leveled_up():
						self.monster.hit_points -= 2
					else:
						self.monster.hit_points -= 1
			# If not a good attack tell the player
			else:
				print("Player attack was not successfull!")
		# If he rest's:
		elif move == 'R':
			# Call the player.rest() method
			self.player.rest()
		# If he quit's, exit the game
		elif move == 'Q':
			sys.exit()
		# If anything else, re-run this method 
		else:
			self.player_turn()	

	def cleanup(self):
		# If monster has no more hit points:
		if self.monster.hit_points <= 0:
			# up the player's experience
			self.player.experience += self.monster.experience
			print("You killed {}".format(self.monster))
			# print a message
			print("Player gained {} XP!".format(self.monster.experience))
			# Get a new monster
			self.monster = self.get_next_monster()

	def __init__(self):
		self.setup()

		while self.player.hit_points and (self.monster or self.monsters):
			print('=' * 20)
			print(self.player)
			self.monster_turn()
			print('=' * 20)
			self.player_turn()
			self.cleanup()
			print('=' * 20)

		if self.player.hit_points:
			print("You win!")
		elif self.monster or self.monsters:
			print("You loose!")

		sys.exit()


Game()






















