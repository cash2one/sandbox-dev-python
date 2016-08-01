from multiprocessing import Queue, Process
import random

def generate(q):
	while True:
		value = random.randrange(10)
		q.put(value)
		print "Value added to queue: %s" % (value)

def reader(q):
	while True:
		value = q.get()
		print "Value from queue: %s" % (value)


queue = Queue()
p1 = Process(target=generate, args=(queue,))
p2 = Process(target=reader, args=(queue,))

p1.start()
p2.start()

