#!/usr/bin/python
'''file description ...'''

import time

def fab(max):
    l = []
    n, a, b = 0, 0, 1
    while n < max:
        l.append(b)
        a, b = b, a + b
        n = n + 1
    return l

def fab1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

def p(f):
    print f
    for i in f:
        print i

f0 = fab(5)
f1 = fab1(5)
# p(f0)
# p(f1)

# from timeit import Timer
# f0 = Timer("fab(100)", "from __main__ import fab")
# f1 = Timer("fab1(100)", "from __main__ import fab1")
# print f0.timeit(10000)
# print f1.timeit(10000)


class Fab(object):

    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()
	
	