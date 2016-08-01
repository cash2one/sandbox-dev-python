#!/usr/bin/python

import thread
import time

global_value = 0

def run( threadName):
   global global_value
   local_copy = global_value
   print "%s with value %s" % (threadName, local_copy)
   global_value = local_copy + 1


for i in range(10):
   thread.start_new_thread( run, ("Thread-" + str(i), ) )

# We need to keep the program working, otherwise the threads won't live
while 1:
   pass