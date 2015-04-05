import Map
import sys


current_room = 1
limits = Map.get_limits(current_room)
doors = Map.get_doors(current_room)
inDoor = doors[0]
outDoor = doors[1]
pos = [inDoor[0],inDoor[1]]
available_keys = ['a','s','d','w','exit']
clues_places = []
for clue in Map.get_clues(current_room):
	clues_places.append(clue)
doors_places= [[inDoor[0],inDoor[1]],[outDoor[0],outDoor[1]]]

def action(a):

	def move_up():
		if pos[1] < limits[1]:
			pos[1] +=1
		else:
			print('There is a wall!')		
	def move_down():
		if pos[1] > 0:
			pos[1] -=1
		else:
			print('There is a wall!')
	def move_right():
		if pos[0] < limits[0]:
			pos[0] += 1
		else:
			print('There is a wall!')
	def move_left():
		if pos[0] > 0:
			pos[0] -=1
		else:
			print('There is a wall!')

	def quit_game():
		sys.exit()

	actions = {'w':move_up,
	's':move_down,
	'd':move_right,
	'a':move_left,
	'exit':quit_game}

	return actions[a]

def user_input():
	while True:
		key = input('>')
		if key in available_keys:
			a = action(key)
			a()
			evet_scanner()
			print(pos)
		else:
			print('Enter an available key')

def evet_scanner():
	if pos in clues_places or pos in doors_places:
		print('Important place')
	else:
		print('Common place')

