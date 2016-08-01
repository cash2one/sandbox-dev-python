import time
import sys

option = sys.argv[1]

words =  [str(x) for x in xrange(1000000)]

if option == '1':
	full_doc = ""
	init = time.clock()
	for w in words:
		full_doc += w
	print "Time using for-loop: %s" % (time.clock() - init)

else:
	init = time.clock()
	full_doc = "".join(words)
	print "Time using join: %s" % (time.clock() - init)
