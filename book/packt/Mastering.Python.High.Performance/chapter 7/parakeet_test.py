from parakeet import jit
import random
import numpy as np
import time

@jit 
def allpairs_dist_prkt(X,Y):
  def dist(x,y):
    return np.sum( (x-y)**2 )
  return np.array([[dist(x,y) for y in Y] for x in X])

def allpairs_dist_py(X,Y):
  def dist(x,y):
    return np.sum( (x-y)**2 )
  return np.array([[dist(x,y) for y in Y] for x in X])

input_a =  [ random.random()  for x in range(0, 10000)] 
input_b =  [ random.random()  for x in range(0, 10000)] 

print "----------------------------------------------"
init = time.clock()
allpairs_dist_py(input_a, input_b)
end = time.clock()
print "Total time pure python: %s" % (end - init)

print 
init = time.clock()
allpairs_dist_prkt(input_a, input_b)
end = time.clock()
print "Total time parakeet: %s" % (end - init)
print "----------------------------------------------"
