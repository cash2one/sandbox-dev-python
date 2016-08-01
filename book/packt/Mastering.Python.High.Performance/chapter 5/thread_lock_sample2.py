#!/usr/bin/python

import thread
import time

global_value = 0

def run( threadName, lock ):
   global global_value
   lock.acquire()
   local_copy = global_value
   print "%s with value %s" % (threadName, local_copy)
   global_value = local_copy + 1
   lock.release()


lock = thread.allocate_lock()

for i in range(10):
   thread.start_new_thread( run, ("Thread-" + str(i), lock) )

# We need to keep the program working, otherwise the threads won't live
while 1:
   pass