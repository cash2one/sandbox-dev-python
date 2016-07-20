import math
import time

TIMES = 10000000

init = time.clock()
for i in range(TIMES):
    value = math.sqrt(i * math.fabs(math.sin(i - math.cos(i))))

print "No function: %s" % ( init - time.clock())

def calcMath(i):
    return math.sqrt(i * math.fabs(math.sin(i - math.cos(i))))
init = time.clock()

for i in range(TIMES):
    value = calcMath(i)
print "Function: %s" % ( init - time.clock())
