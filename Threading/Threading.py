from threading import Thread
import time

def timer(name, delay, repeat):
	print ('Timer: "' + name + ' Startd')
	while repeat > 0:
		time.sleep(delay)
		print(name + ': ' + str(time.ctime(time.time())))
		repeat -=1
	print('Timer: ' + name + ' is completed')



def Main():
	#  We create the threads
	t1 = Thread(target = timer, args=('Timer 1', 1, 5))
	t2 = Thread(target = timer, args=('Timer 2', 2, 5))
	#  Make them to start
	t1.start()
	t2.start()

	print('Main completed')

Main()