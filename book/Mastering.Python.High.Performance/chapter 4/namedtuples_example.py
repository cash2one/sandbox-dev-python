import time
import collections


class Obj(object):
  def __init__(self, i):
    self.i = i
    self.l = []
all = {}

init = time.clock()
for i in range(1000000):
  all[i] = Obj(i)
print "Regular Objects: %s" % (time.clock() - init)


Obj = collections.namedtuple('Obj', 'i l')

all = {}
init = time.clock()
for i in range(1000000):
  all[i] = Obj(i, [])
print "Regular Objects: %s" % (time.clock() - init)
