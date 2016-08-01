#!/usr/bin/python

import multiprocessing

def run( pname ):
	print pname

for i in range(10):
	p = multiprocessing.Process(target=run, args=("Process-" + str(i), ))
	p.start()
	p.join()