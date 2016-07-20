import multiprocessing
import time

def first():
	print "There is no problem here"

def second():
	raise RuntimeError("Error raised!")

def third():
	time.sleep(3)
	print "This process will be terminated"

workers = [ multiprocessing.Process(target=first), multiprocessing.Process(target=second), multiprocessing.Process(target=third)]

for w in workers:
	w.start()

workers[-1].terminate()

for w in workers:
	w.join()


for w in workers:
	print w.exitcode
