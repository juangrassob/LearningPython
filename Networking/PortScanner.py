import threading
from queue import Queue
import socket



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = 'localhost'


def pscan(port):

	try:
		s.connect((server,port))
		return True
	except:
		return False


def threader():
	while True:
		worker = q.get()
		if pscan(worker):
			print('Port: ',worker,' is open !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
		else:
			print('Port: ',worker,' is closed')
		q.task_done()

q = Queue()
for x in range(100): 
	t = threading.Thread(target = threader) 
	t.daemon = True 
	t.start()

for x in range(10000):
	q.put(x)

q.join()

print('All the ports were scaned')