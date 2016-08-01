import time
import random
from ctypes import cdll


libc = cdll.LoadLibrary('libc.so.6') #linux systems
#libc = cdll.msvcrt #windows systems

init = time.clock()
randoms = [random.randrange(1, 100) for x in xrange(1000000)]
print "Pure python: %s seconds" % (time.clock() - init)

init = time.clock()
randoms = [(libc.rand() % 100) for x in xrange(1000000)]
print "C version : %s seconds" % (time.clock() - init)