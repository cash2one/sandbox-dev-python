import threading
import time


class ThreadA(threading.Thread):

	def __init__(self, event):
		threading.Thread.__init__(self)
		self.event = event


	def run(self):
		count = 0
		while count < 5:
			time.sleep(1)
			if self.event.is_set():
				print "A"
				self.event.clear()
			count += 1

class ThreadB(threading.Thread):

	def __init__(self, evnt):
		threading.Thread.__init__(self)
		self.event = evnt


	def run(self):
		count = 0
		while count < 5:
			time.sleep(1)
			if not self.event.is_set():
				print "B"
				self.event.set()
			count += 1


event = threading.Event()

ta = ThreadA(event)
tb = ThreadB(event)

ta.start()
tb.start()

