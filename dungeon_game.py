import logging
import random

loggin.basicConfig(filename = 'dungeon_game.log', level = logging.DEBUG)

MOVES = ['LEFT','RIGHT','UP','DOWN']

CELLS = [(0,0),(0,1),(0,2),
		 (1,0),(1,1),(1,2),
		 (2,0),(2,1),(2,2)]

def get_locations():
	# monster = random
	monster = random.choice(CELLS)
	# door = random
	door = random.choice(CELLS)
	# start = random
	start = random.choice(CELLS)

	#if monster, door or start are the same do it again
	while monster == door or monster == start or door == start:
		# monster = random
		monster = random.choice(CELLS)
		# door = random
		door = random.choice(CELLS)
		# start = random
		start = random.choice(CELLS)


	#return monster, door, start
	return monster, door, start

def move_player(p,move):
	# Get players current location
	x,y = p
	# If move is LEFT -> y - 1
	if move == 'LEFT':
		y -= 1
	# If move is RIGHT -> y + 1
	elif move == 'RIGHT':
		y += 1
	# If move is UP -> x - 1
	elif move == 'UP':
		x -= 1
	# If move is DOWN -> x + 1
	elif move == 'DOWN':
		x += 1
	return x,y



def get_moves(player):
	x,y = player
	m = MOVES
	# if x == 0 remove UP
	if x == 0:
		m.remove('UP')
	# if x == 2 remove DOWN
	if x == 2:
		m.remove('DOWN')
	# if y == 0 remove LEFT
	if y == 0:
		m.remove('LEFT')
	# if x == 2 remove RIGHT
	if y == 2:
		m.remove('RIGHT')

	return m

def draw_map(player):
	print(' _ _ _')
	tile = '|{}'
	
	for idx,cell in enumerate(CELLS):
		if idx in [0,1,3,4,6,7]:
			if cell == player:
				print(tile.format('X'), end='')
			else:
				print(tile.format('_'), end='')
		else:
			if cell == player:
				print(tile.format('X|'))
			else:
				print(tile.format('_|'))


				


monster,door,player = get_locations()

logging.info('monster: {}; door: {}; player: {}'.format(monster,door,player))

print("Welcome to the dungeon!")

while 1:
	av_moves = get_moves(player)

	print("You are currently in room {}".format(player)) # fill with player position
	print("You can move {}".format(av_moves)) # fill in with available moves
	print("Enter \"QUIT\" to quit")

	print()
	draw_map(player)
	print()

	move = input("> ")
	move = move.upper()

	if move == 'QUIT':
		break

	# If its good move, change player position
	if move in av_moves:
		player = move_player(player,move)
	# If its good move, change player position
	else:
		print("BAD MOVE. TRY AGAIN!")
		continue


	# If new player position is the door, they win
	if player == door:
		print("YOU WIN!!!")
		break
	# If new player position is the monster, they loose
	elif player == monster:
		print("YOU LOOSE!!!")
		break
	# Otherwise, continue
	else:
		continue