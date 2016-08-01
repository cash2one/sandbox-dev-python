import random
import time


#Generate 2 random lists of random elements
list1 = [ [random.randrange(0, 100), chr(random.randrange(32, 122))] for x in range(100000)]
list2 = [ [random.randrange(0, 100), chr(random.randrange(32, 122))] for x in range(100000)]

#sort by string, using a comparison function
init = time.clock()
list1.sort(cmp=lambda a,b: cmp(a[1], b[1]))
print "Sort by comp: %s" % (time.clock() - init)


#sort by key, using the string element as key
init = time.clock()
list2.sort(key=lambda a: a[1])
print "Sort by key: %s" % (time.clock() - init)
