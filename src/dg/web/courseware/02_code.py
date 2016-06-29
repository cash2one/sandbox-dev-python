#!/usr/bin/python
'''file description...'''

#########位置参数############
def foo(a1, a2, a3):
	print a1, a2, a3
foo(1,3,2)

#########默认值参数############
def foo(a1=1, a2=2, a3=3):
	print a1, a2, a3
foo()	
foo(1,3,2)

def foo(a1, a2, a3=3):
	print a1, a2, a3
foo(1,2,4)
foo(1,2,a3=4)	
foo(1,2)

#########动态参数############
def foo(*args):
	print type(args)
	for i in args:
		print i
foo(1)
foo(1, 'a', True, None)

def foo(**args):
	print type(args)
	for k,v in args.items():
		print k,v
foo(k1=1)
foo(k1=1, k2='a', k3=True, k4=None)

def foo(*arg1, **arg2):
	for i in arg1:
		print i
	for k,v in arg2.items():
		print k,v
foo(1)
foo(k1=1)
foo(100, 200, k3=True, k4=None)

def foo(a, k=100, *arg1, **arg2):
	print a, k, arg1, arg2
foo(1) 

#########用户输入############
s = raw_input('Please input something:')  
print s
s = input('Please input something:')
print s

#########文件操作############
f = open('1.txt', 'a')
dir(f)
f.write('sdfsdfsdf\r\nfsdfsdf')
f.close()

f = open('1.txt', 'r')  ##rb
dir(f)
for l in f:
	print l
f.close()

f = open('1.txt', 'w')  ##rw
dir(f)
f.write('sdfsdfsdf\r\nfsdfsdf\r\n2342423423')
f.close()

f = open('1.txt', 'r')  ##rb
dir(f)
for l in f:
	print l
f.close()

#########map############
s1=[2,3,5,3,7,9,4]
s2=[5,3,5,4,7,6,8]
s3=[9,6,5,3,2,1,5]
s=map(lambda x,y,z:x+y+z, s1, s2, s3)
print s

#########reduce############
s1=[1,2,3,4,5,6,7,8,9,10]
s=reduce(lambda x,y:x+y, s1)
print s

#########filter############
s1=[1,2,3,4,5,6,7,8,9,10]
s=filter(lambda x:x%2==0, s1)
print s

#########os############
import os
print dir(os)
os.mkdir('d:\pytest')
l = os.listdir('d:\pytest')
print l

#########sys############
import sys
print dir(sys)
print sys.getdefaultencoding()
print sys.path

#########re############
import re
text = "JGood is a handsome boy, he is cool, clever, and so on..."
m = re.match(r"(\w+)\s", text)
if m:
	print m.group(0), '\n', m.group(1)
else:
	print 'not match'

#########json############
import json
obj = [[1,2,3],123,123.123,'abc',{'key1':(1,2,3),'key2':(4,5,6)}]
print obj
encodedjson = json.dumps(obj)
print type(encodedjson)
print encodedjson
decodejson = json.loads(encodedjson)
print type(decodejson)

#########pickle############
import pickle
print dir(pickle)
l = [1,2,3,4,5]
f = open('d:/1.txt', 'w')
pickle.dump(l, f)
f.close()
f = open('d:/1.txt', 'r')
ll = pickle.load(f)
f.close()
dir(ll)
print ll

#########异常############
import sys, traceback
try:
	1/0
except IOError, ex:
	print ex.message
except (Exception, IOError), ex:
	print ex.message
	traceback.print_exc()
	sys.exc_info()
except Exception:
	print 'do something for Exception'
	raise ValueError, 'invalid argument'
except:
	print 'do something for Default Exception'
finally:
	print 'Done'
	
#########自定义异常############
class MyException(Exception):  
	def __init__(self, length, least):  
		Exception.__init__(self)  
		self.length = length  
		self.least = least  

try:  
	raise MyException(5, 5)   
except MyException, ex:
	print type(ex) 
	print dir(ex) 
except Exception:  
	print 'nothing'
	
#########内省############
class MyClass(object):
	def __init__(self):
		pass
	def __del__(self):
		pass
	def foo(self):
		print 'in foo'
	def __str__(self):
		return 'myclass str'
		
mycls = MyClass()
print id(mycls)
print str(mycls)
print dir(mycls)
print help(mycls)
print type(mycls)
print hasattr(mycls, 'foo')
print getattr(mycls, 'foo')
print isinstance(mycls, MyClass)
print isinstance(mycls, object)
	
	