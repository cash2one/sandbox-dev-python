from multiprocessing import Process, Event, Pool
import time


event = Event()
event.set()

def worker(i, e):
	if e.is_set():
		time.sleep(0.1)
		print "A - %s" % (time.time())
		e.clear()
	else:
		time.sleep(0.1)
		print "B - %s" % (time.time())
		e.set()


pool = Pool(3)
pool.map(worker, [ (x, event) for x in range(9)])
