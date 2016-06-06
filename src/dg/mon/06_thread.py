from time import ctime,sleep
from thread import start_new_thread
def loop1():
    print "enter loop1:",ctime();
    sleep(3);
    print "leave loop1:",ctime();

def loop2():
    print "enter loop2:",ctime();
    sleep(5);
    print "leave loop2:",ctime();

def main():
    print "main begin:",ctime();
    start_new_thread(loop1, ());
    start_new_thread(loop2,());
    sleep(8);
    print "main end:",ctime();

if __name__=="__main__":
    main()


import threading,time
from time import sleep, ctime
def now() :
    return str( time.strftime( '%Y-%m-%d %H:%M:%S' , time.localtime() ) )

def test(nloop, nsec):
    print 'start loop', nloop, 'at:', now()
    sleep(nsec)
    print 'loop', nloop, 'done at:', now()

def main():
    print 'starting at:',now()
    threadpool=[]

    for i in xrange(10):
        th = threading.Thread(target= test,args= (i,2))
        threadpool.append(th)

    for th in threadpool:
        th.start()

    for th in threadpool :
        threading.Thread.join( th )

    print 'all Done at:', now()

if __name__ == '__main__':
        main()
		
		
import threading ,time
from time import sleep, ctime
def now() :
    return str( time.strftime( '%Y-%m-%d %H:%M:%S' , time.localtime() ) )

class myThread (threading.Thread) :
      """docstring for myThread"""
      def __init__(self, nloop, nsec) :
          super(myThread, self).__init__()
          self.nloop = nloop
          self.nsec = nsec

      def run(self):
          print 'start loop', self.nloop, 'at:', ctime()
          sleep(self.nsec)
          print 'loop', self.nloop, 'done at:', ctime()
def main():
     thpool=[]
     print 'starting at:',now()
    
     for i in xrange(10):
         thpool.append(myThread(i,2))
         
     for th in thpool:
         th.start()
   
     for th in thpool:
         th.join()
    
     print 'all Done at:', now()

if __name__ == '__main__':
        main()
		


import threadpool
import time
import urllib2
 
urls = [
    'http://www.google.com', 
    'http://www.amazon.com', 
    'http://www.ebay.com', 
    'http://www.alibaba.com', 
    'http://www.reddit.com'
]
 
def myRequest(url):
    resp = urllib2.urlopen(url)
    print url, resp.getcode()
 
 
def timeCost(request, n):
  print "Elapsed time: %s" % (time.time()-start)
 
start = time.time()
pool = threadpool.ThreadPool(5)
reqs = threadpool.makeRequests(myRequest, urls, timeCost)
[ pool.putRequest(req) for req in reqs ]
pool.wait()
		

		

from threading import Lock, Thread
lock = Lock()
some_var = 0  
class IncrementThread(Thread):
    def run(self):
        #we want to read a global variable
        #and then increment it
        global some_var
        lock.acquire()
        read_value = some_var
        print "some_var in %s is %d" % (self.name, read_value)
        some_var = read_value + 1
        print "some_var in %s after increment is %d" % (self.name, some_var)
        lock.release()
  
def use_increment_thread():
    threads = []
    for i in range(50):
        t = IncrementThread()
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print "After 50 modifications, some_var should have become 50"
    print "After 50 modifications, some_var is %d" % (some_var,)
  
use_increment_thread()


import threading
import time
 
event = threading.Event()
 
def func():
    # 等待事件，进入等待阻塞状态
    print '%s wait for event...' % threading.currentThread().getName()
    event.wait()
    
    # 收到事件后进入运行状态
    print '%s recv event.' % threading.currentThread().getName()
 
t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)
t1.start()
t2.start()
 
time.sleep(2)
 
# 发送事件通知
print 'MainThread set event.'
event.set()




import threading
import time
 
# 商品
product = None
# 条件变量
con = threading.Condition()
 
# 生产者方法
def produce():
    global product
    
    if con.acquire():
        while True:
            if product is None:
                print 'produce...'
                product = 'anything'
                
                # 通知消费者，商品已经生产
                con.notify()
            
            # 等待通知
            con.wait()
            time.sleep(2)
 
# 消费者方法
def consume():
    global product
    
    if con.acquire():
        while True:
            if product is not None:
                print 'consume...'
                product = None
                
                # 通知生产者，商品已经没了
                con.notify()
            
            # 等待通知
            con.wait()
            time.sleep(2)
 
t1 = threading.Thread(target=produce)
t2 = threading.Thread(target=consume)
t2.start()
t1.start()

