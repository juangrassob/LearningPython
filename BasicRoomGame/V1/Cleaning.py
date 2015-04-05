import Map
import os
import Actions

def clean_rooms():
	number = Map.number_of_rooms()
	os.remove('number_of_rooms')
	if number != 0:
		for i in range(number):
			os.remove('room_n'+str(i+1))
	Actions.current_room = 1

