#!/bin/python
#__encoding=utf-8__

from threading import Thread, RLock
import threading
import Queue
import os
import time

rlock = threading.RLock()
curPosition = 0


class writer(Thread):
    def __init__(self, res, num):
        Thread.__init__(self)
        self.res = res
        self.num = num
        self.q = self.res.q

    def run(self):
        while True:
            s = []
            while not self.q.empty():
                print 'get string from queue...'
                s.append(self.q.get() + '\n')

            if s:
                print 'request lock'
                rlock.acquire()
                f = open(self.res.fn, self.res.m)
                for i in s:
                    print 'thread-%s-write: %s' % (self.num, i)
                    f.write(i)
                f.close()
                rlock.release()
            else:
                time.sleep(1)
                print 'waiting for write...'
                continue


class reader(Thread):
    def __init__(self, res, num):
        Thread.__init__(self)
        self.res = res
        self.num = num

    def run(self):
        global curPosition
        fstream = open(self.res.fn, self.res.m)
        while True:
            rlock.acquire()
            startPosition = curPosition
            self.getFileSize()
            curPosition = endPosition = (startPosition + self.res.blockSize) if (startPosition + self.res.blockSize) < self.fileSize else self.fileSize
            rlock.release()
            if startPosition == self.fileSize:
                time.sleep(1)
                print 'waiting for read...'
                continue
            elif startPosition != 0:
                fstream.seek(startPosition)
                fstream.readline()
            pos = fstream.tell()
            while pos < endPosition:
                line = fstream.readline()
                print 'thread-%s-read: %s' % (self.num, line)
                pos = fstream.tell()
        fstream.close()

    def getFileSize(self):
        fstream = open(self.res.fn, 'r')
        fstream.seek(0, os.SEEK_END)
        self.fileSize = fstream.tell()
        fstream.close()


class resource(object):
    def __init__(self, fn, m, q=None):
        self.fn = fn
        self.m = m
        self.blockSize = 100
        self.q = q

if __name__=='__main__':
    q = Queue.Queue(maxsize=100)
    res = resource(r'e:\pt.txt', 'a+', q)
    ts = []
    for i in range(5):
        w = writer(res, i)
        ts.append(w)

    for t in ts:
        t.start()

    for i in range(len(ts)):
        q.put('thread %s contentcontent' % i)

    time.sleep(1)
    res = resource(r'e:\pt.txt', 'r')
    rs = []
    for i in range(3):
        r = reader(res, i)
        rs.append(r)

    for r in rs:
        r.start()

    for i in range(len(ts)):
        q.put('thread %s 333' % i)
