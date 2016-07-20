#!/usr/bin/python

import threading
import time

global_value = 0

def run( threadName, lock ):
	global global_value
	lock.acquire()
	local_copy = global_value
	print "%s with value %s" % (threadName, local_copy)
	global_value = local_copy + 1
	lock.release()


lock = threading.Lock()

for i in range(10):
   t = threading.Thread( target=run, args=("Thread-" + str(i), lock) )
   t.start()
