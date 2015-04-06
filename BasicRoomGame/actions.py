import map
import sys
import random
import time

current_room = 0
limits = []
pos = [0,0]
key = False
lives = 50
available_keys = ['a','s','d','w','exit','open','clue','key']

def next_room():
	global current_room
	global pos
	global limits
	global key
	key = False
	map.new_room(random.randint(5,10))
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
		if pos[1] < limits:
			pos[1] +=1
		else:
			print('There is a wall!')		
	def move_down():
		if pos[1] > 0:
			pos[1] -=1
		else:
			print('There is a wall!')
	def move_right():
		if pos[0] < limits:
			pos[0] += 1
		else:
			print('There is a wall!')
	def move_left():
		if pos[0] > 0:
			pos[0] -=1
		else:
			print('There is a wall!')
	def openDoor():
		if pos == map.get_inDoor(current_room):
			if current_room != 1:
				back_room()
				print('Welcome to room n: '+str(current_room))
			else:
				print('You are at room n: 1 !!!')
		if pos == map.get_outDoor(current_room):
			if key:
				next_room()
				print('Welcome to room n: '+str(current_room))
			else:
				print('You have to find the key')
	def readClue():
		global lives
		lives -= 1
		print('You loose a live, now you have: ', lives)
		if pos in map.get_Clues(current_room):
			cords_key = map.get_key(current_room)
			dist_key  = abs(pos[0] - cords_key[0]) + abs(pos[1] - cords_key[1])
			print('Your distance to the key is: ',str(dist_key))
	def pickKey():
		global key
		global lives 
		lives -= 1
		print('You loose a live, now you have: ', lives)
		if pos ==map.get_key(current_room):
			key = True
			print('You found the key!!!')

	def quit_game():
		sys.exit()

	actions = {'w':move_up,
	's':move_down,
	'd':move_right,
	'a':move_left,
	'open':openDoor,
	'clue':readClue,
	'key':pickKey,
	'exit':quit_game}

	return actions[a]
def user_input():
	while True:
		key = input('>')
		if key in available_keys:
			a = action(key)
			a()
			event_scanner()
			if lives == 0:
				print('You loose :)')
				time.sleep(2)
				sys.exit()
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



print('''
You are in a room, use a,s,d,w to move arrownd ir.
You must find the key to open the outDoor
open to open a door.
clue to read a clue 
key to pick the key
exit to exit the quit the game 
Each time you read a clue or try to pick the key, you loose a live
If you loose all your lives you are dead
Have fun :)
''')
next_room()
user_input()