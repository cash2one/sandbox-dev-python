import math
import time
from collections import defaultdict
import itertools

trig_lookup_table = defaultdict(lambda: 0) 


def drange(start, stop, step):
    assert(step != 0)
    sample_count = math.fabs((stop - start) / step)
    return itertools.islice(itertools.count(start, step), sample_count)


def complexTrigFunction(x):
	return math.sin(x) * math.cos(x)**2

	
def lookUpTrig(x):
	return trig_lookup_table[int(x)]


for x in range(-1000, 1000):
	trig_lookup_table[x] = complexTrigFunction(x)

trig_results = []
lookup_results = []

init_time = time.clock()
for x in drange(-100, 100, 0.1):
	trig_results.append(complexTrigFunction(x))
print "Trig results: %s" % (time.clock() - init_time)

init_time = time.clock()
for x in drange(-100, 100, 0.1):
	lookup_results.append(lookUpTrig(x))
print "Lookup results: %s" % (time.clock() - init_time)

for idx in range(0, len(lookup_results)):
	print "%s\t%s" % (trig_results [idx], lookup_results[idx])


