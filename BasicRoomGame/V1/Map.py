import pickle
import random

def new_room():
	add_room()
	map_new_room()
def number_of_rooms():
	try:
		f = open('number_of_rooms','r')
		number = f.read()
		f.close()
		return int(number)
	except:
		f = open('number_of_rooms','w')
		f.write('0')
		f.close()
		return 0
def add_room():
	nr = number_of_rooms()
	f = open('number_of_rooms','w')
	n = str(nr+1)
	f.write(n)
	f.close()
def map_new_room():
	room = []
	a = 10
	b = 10
	clues_number = 5
	x = a
	y = b
	room.append(x) #  X
	room.append(y) #  Y
	inDoor = []
	outDoor = []
	while inDoor == outDoor:
		inDoor = [random.randint(0,b),random.randint(0,b),'I']
		outDoor = [random.randint(0,b),random.randint(0,b),'O']
	doors = [inDoor,outDoor]
	room.append(doors)
	clues = []
	for i in range(clues_number):
		clues.append([random.randint(0,b),random.randint(0,b)])

	room.append(clues)
	key = random.choice(clues)
	room.append(key)

	file = 'room_n'+str(number_of_rooms())
	pickle.dump(room,open(file,'wb'))
	print(room)
def get_limits(room_number):
	room = pickle.load(open('room_n'+str(room_number),'rb'))
	limits = [room[0],room[1]]
	return limits
def get_doors(room_number):
	room = pickle.load(open('room_n'+str(room_number),'rb'))
	doors = room[2]
	return doors
def get_clues(room_number):
	room = pickle.load(open('room_n'+str(room_number),'rb'))
	clues = room[3]
	return clues
def get_key(room_number):
	room = pickle.load(open('room_n'+str(room_number),'rb'))
	key = room[4]
	return key
new_room()
