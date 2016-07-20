import time


init = time.clock()
numbers = [x for x in range(10)]
print "comp 10: %s" % (time.clock() - init)
init = time.clock()
numbers = [x for x in range(100)]
print "comp 100: %s" % (time.clock() - init)
init = time.clock()
numbers = [x for x in range(1000)]
print "comp 1000: %s" % (time.clock() - init)
init = time.clock()
numbers = [x for x in range(10000)]
print "comp 10000: %s" % (time.clock() - init)
init = time.clock()
numbers = [x for x in range(100000)]
print "comp 100000: %s" % (time.clock() - init)
init = time.clock()
numbers = (x for x in range(10))
print "gen 10: %s" % (time.clock() - init)
init = time.clock()
numbers = (x for x in range(100))
print "gen 100: %s" % (time.clock() - init)
init = time.clock()
numbers = (x for x in range(1000))
print "gen 1000: %s" % (time.clock() - init)
init = time.clock()
numbers = (x for x in range(10000))
print "gen 10000: %s" % (time.clock() - init)
init = time.clock()
numbers = (x for x in range(100000))
print "gen 100000: %s" % (time.clock() - init)

init = time.clock()
numbers = (x for x in range(10**10))
print "gen 10**10: %s" % (time.clock() - init)

