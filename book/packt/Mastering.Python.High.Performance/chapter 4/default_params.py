import time
import math

def degree_sin(deg):
	return math.sin(deg * math.pi / 180.0) * math.cos(deg * math.pi / 180.0)


def degree_sin_opt(deg, factor=math.pi/180.0, sin=math.sin, cos = math.cos):
	return sin(deg * factor) * cos(deg * factor)


normal_times = []
optimized_times = []


for y in range(100):
	init = time.clock()
	for x in range(1000):
		degree_sin(x)
	normal_times.append(time.clock() - init)


	init = time.clock()
	for x in range(1000):
		degree_sin_opt(x)
	optimized_times.append(time.clock() - init)


print "Normal function: %s" % (reduce(lambda x, y: x + y, normal_times, 0) / 100)
print "Optimized function: %s" % (reduce(lambda x, y: x + y, optimized_times, 0 ) / 100)
