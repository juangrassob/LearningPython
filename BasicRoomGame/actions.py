import map
import sys

current_room = 0
limits = []
pos = [0,0]
available_keys = ['a','s','d','w','exit']

def next_room():
	global current_room
	global pos
	global limits
	current_room += 1
	limits = map.get_limits(current_room)
	pos = map.get_inDoor(current_room)

def back_room():
	global current_room
	global pos
	global limits
	current_room -= 1
	limits = map.get_limits(current_room)
	pos = map.get_outDoor(current_room)
def action(a):
	def move_up():
		if pos[1] <= limits:
			pos[1] +=1
		else:
			print('There is a wall!')		
	def move_down():
		if pos[1] >= 0:
			pos[1] -=1
		else:
			print('There is a wall!')
	def move_right():
		if pos[0] <= limits:
			pos[0] += 1
		else:
			print('There is a wall!')
	def move_left():
		if pos[0] >= 0:
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
			event_scanner()
			print(pos)
		else:
			print('Enter an available key')
def event_scanner():
	if pos == map.get_inDoor(current_room):
		print('You are in the inDoor')
	if pos == map.get_outDoor(current_room):
		print('You are in the outDoor')	
	if pos in map.get_Clues(current_room):
		print('You found a clue')




next_room()
user_input()