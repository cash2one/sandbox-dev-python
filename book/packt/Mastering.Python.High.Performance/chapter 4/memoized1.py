import math
import time
import random

class Memoized:
  def __init__(self, fn):
    self.fn = fn
    self.results = {}


  def __call__(self, *args):
    key = ''.join(map(str, args[0]))
    try:
      return self.results[key]
    except KeyError:
      self.results[key] = self.fn(*args)
    return self.results[key]


@Memoized
def twoParamsMemoized(values, period):
  totalSum = 0
  for x in range(0, 100):
    for v in values:
      totalSum = math.pow((math.sqrt(v) * period), 4) + totalSum
  return totalSum



def twoParams(values, period):
  totalSum = 0
  for x in range(0, 100):
    for v in values:
      totalSum = math.pow((math.sqrt(v) * period), 4) + totalSum
  return totalSum



def performTest():
    valuesList = []
    for i in range(0, 10):
        valuesList.append(random.sample(xrange(1, 101), 10))

    start_time = time.clock()
    for x in range(0, 10):
      for values in valuesList:
          twoParamsMemoized(values, random.random())
    end_time = time.clock() - start_time
    print "Fixed params, memoized: %s" % (end_time)

    start_time = time.clock()
    for x in range(0, 10):
      for values in valuesList:
          twoParams(values, random.random())
    end_time = time.clock() - start_time
    print "Fixed params, without memoizing: %s" % (end_time)


    start_time = time.clock()
    for x in range(0, 10):
      for values in valuesList:
          twoParamsMemoized(random.sample(xrange(1,2000), 10), random.random())
    end_time = time.clock() - start_time
    print "Random params, memoized: %s" % (end_time)

    start_time = time.clock()
    for x in range(0, 10):
      for values in valuesList:
          twoParams(random.sample(xrange(1,2000), 10), random.random())
    end_time = time.clock() - start_time
    print "Random params, without memoizing: %s" % (end_time)


performTest()