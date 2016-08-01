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


reverse_indexes = {}
for x in range(-1000, 1000):
	trig_lookup_table[x] = complexTrigFunction(math.pi * x / 1000)


complex_results = []
lookup_results = []

init_time = time.clock()
for x in drange(-10, 10, 0.1):
	complex_results .append(complexTrigFunction(x))
print "Complex trig function: %s" % (time.clock() - init_time)

init_time = time.clock()
factor = 1000 / math.pi
for x in drange(-10 * factor, 10 * factor, 0.1 * factor):
	lookup_results.append(trig_lookup_table[int(x)])
print "Lookup results: %s" % (time.clock() - init_time)

for idx in range(0, len(lookup_results )):
	print "%s\t%s" % (complex_results [idx], lookup_results [idx])


