import threading
import time

class AsyncWrite(threading.Thread):
	def __init__(self, text, out):
		threading.Thread.__init__(self)
		self.text = text
		self.out = out

	def run(self):
		f = open(self.out, "w")
		f.write(self.text + '\n')
		f.close
		time.sleep(2)
		print ('Finished Background file write '+ self.out)

def Main():
	message = input('Enter a string to store:')
	background = AsyncWrite(message, 'out.txt')
	background.start()
	print ('The program can continue to run while ir write another thread.')
	print ( 100 + 500)

	background.join()
	print('Waited until the thread was complete')

Main()
