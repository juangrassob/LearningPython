import pickle
import random
import os


pickle.dump('0',open('number_of_rooms','wb'))

def new_room(clues_number):
	#  Add one room to the total

	old_number = pickle.load(open('number_of_rooms','rb'))
	new_number = int(old_number) + 1
	pickle.dump(new_number,open('number_of_rooms','wb'))
	
	#  Crate the new room and save it as a list

	dimensios = 10 #  10x10 square rooms
	inDoor = [random.randint(0,dimensios),random.randint(0,dimensios)]
	outDoor = [random.randint(0,dimensios),random.randint(0,dimensios)]
	clues = []
	for i in range(clues_number):
		clues_coords = [random.randint(0,dimensios),random.randint(0,dimensios)]
		while (clues_coords == inDoor) or (clues_coords == outDoor):
			clues_coords = [random.randint(0,dimensios),random.randint(0,dimensios)]
		clues.append(clues_coords)
	key = random.choice(clues)
	room = [dimensios,inDoor,outDoor,clues,key]
	file_name = 'room_n'+str(new_number)
	pickle.dump(room,open(file_name,'wb'))

	print(room)


def get_room_number():
	number = pickle.load(open('number_of_rooms','rb'))
	return(int(number))
def get_limits(room_number):
	room = pickle.load(open('room_n'+str(room_number),'rb'))
	limits = room[0]
	return(limits)
def get_inDoor(room_number):
	room = pickle.load(open('room_n'+str(room_number),'rb'))
	coords = room[1]
	return(coords)
def get_outDoor(room_number):
	room = pickle.load(open('room_n'+str(room_number),'rb'))
	coords = room[2]
	return(coords)
def get_Clues(room_number):
	room = pickle.load(open('room_n'+str(room_number),'rb'))
	coords = room[3]
	return(coords)
def get_key(room_number):
	room = pickle.load(open('room_n'+str(room_number),'rb'))
	coords = room[4]
	return(coords)

def clean_room():
	number = get_room_number()
	if number != 0:
		for i in range(number):
			os.remove('room_n'+str(i+1))
	pickle.dump('0',open('number_of_rooms','wb'))

clean_room()
new_room(5)
