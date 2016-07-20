import math
import time


def check_prime(x):
	values = xrange(2, int(math.sqrt(x)))
	for i in values:
		if x % i == 0:
			return False 

	return True


init = time.clock()
numbers_py = [x for x in xrange(1000000) if check_prime(x)]
print "%s" % (time.clock() - init)

