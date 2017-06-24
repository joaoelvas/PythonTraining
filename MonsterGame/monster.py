import random

from combat import Combat

COLORS = ['yeallow','red','blue','green']


class Monster(Combat):

	min_hit_points = 1
	max_hit_points = 1
	min_experience = 1
	max_experience = 1
	weapon = 'sword'
	sound = 'roar'

	# init method
	def __init__(self, **kwargs):
		self.hit_points = random.randint(self.min_hit_points,self.max_hit_points)
		self.experience = random.randint(self.min_experience,self.max_experience)
		self.color = random.choice(COLORS)

		# to add more attributes than the original ones
		for key, value in kwargs.items():
			setattr(self,key,value)

	# called when the object is converted to a string
	# ex. on a print(Monster)
	def __str__(self): 
		return '{} {}, HP: {}, XP: {}'.format(self.color.title(),
												self.__class__.__name__,
												self.hit_points,
												self.experience)

	# returns monster sound
	def battlecry(self):
		return self.sound.upper()


# extends monster
class Goblin(Monster):
	max_hit_points = 3
	max_experience = 2
	sound = 'squeak'

# extends monster
class Troll(Monster):
	min_hit_points = 3
	max_hit_points = 5
	min_experience = 2
	max_experience = 6
	sound = 'growl'

# extends monster
class Dragon(Monster):
	min_hit_points = 5
	max_hit_points = 10
	min_experience = 6
	max_experience = 10
	sound = 'raaaaaaaar'