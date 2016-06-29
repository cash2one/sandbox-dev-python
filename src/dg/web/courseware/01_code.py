#!/usr/bin/python
'''file description ...'''

########变量赋值########
a = 1
b='b'
c=True
d=D=None
print a,b,c,d,D
a,b=b,a
print a,b
print type(a), type(c)  ##变量类型
print isinstance(b, int)  

########分支判断########
a=3
if a==1:
	print 'value is 1'
elif a==2:
	print 'value is 2'
else:
	print 'value is other'
	
b = 2
if b:
	print 'b is True, and value is %s' % b
else:
	print 'b is False'
	
########循环迭代########
for i in range(10):
	print i
	
for i in range(10):
	if i>6:
		break
	if i==5:
		continue
	print i

for i in range(1,10,2):
	print i
	
while True:
	print 'ok'
	break

########函数定义########
def foo():
	print 'hello world'
foo()

def foo(name):
	print 'hello %s' % name
foo('Bob')

s = lambda x:x*2
for i in range(5):
	print s(i)

########类定义########
class cfoo(object):
	def __init__(self, name='Macy'):
		self.name = name
		print 'at init:' + self.name
	def __del__(self):
		self.name = None
		print 'at del:', self.name
	def p(self):
		print self.name
c = cfoo('john')
c.p()
del c

########元组########
t = (1, True, 'a', None)
print t
print t[3]
for i in t:
	print i
print t[:2], t[2:], t[1:3]
	
########列表########
l = [1, True, 'a', None]
print type(l)
l.append(3.14)
print l
del l[2]
print l
l[0] = 100
print l

########字典########
d = {1:1, 'a':'a', 'k': [0,1,2]}
print type(d), d
print d[1]
d['k2'] = 'hello'
print d
del d['a']
print d
d[1] = 10
print d

########字符串操作########
a = 'hello' + ' Bob'
print a
s = '1234567890'
print s[3:], s[:5], s[3:7], s[-1]
b = 'my name is %s, and age is %i' % ('John', 25) 
print b
c = 'value of name is %(name)s' % {'name':'macy'}
print c
d = 'hello ' * 5
print d

########帮助########
d = {}
print dir(d)
print help(d.update)
print id(d)
