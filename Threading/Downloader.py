import threading
from queue import Queue
import time

links = ['link_1','link_2','link_3','link_4','link_5','link_6','link_7']

def downloader(worker): #  The function that 'downlad' the content of the links
	print('Downlading: ',str(worker))
	time.sleep(2) #  Simulate that we are downloading something
	print('You just download: ',str(worker))

def threader(): #  Each time a thread is free, it thread the function
	while True:
		worker = q.get() #  The worker get a item of the queue
		downloader(worker) # Call the function Downloader with that specific worker
		q.task_done()  #  Tell that we just finished a task

q = Queue() # Create the queue

for x in range(3): #  I create 3 threads just because want
	t = threading.Thread(target = threader) #  Create the thread
	t.daemon = True #  Say that the thread is a deamon so it die mein Main ends
	t.start() #  Put the thread to work

for l in links: 
	q.put(l) #  Add each item in links to the queue

q.join() #  The program dont contine until all the tasks are donde

print ('All the downloads are completed')

