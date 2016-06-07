#!/usr/bin/python
'''file description ...'''

#!/usr/bin/python
# encoding:utf-8


print '=====lambda====='
c = lambda x: x*2
print c([3])

c = lambda **x: 'more args' if len(x)>1 else 'one arg'
print c(x=1)
print c(x=1,y=2,)

c = lambda *x: [i for i in x if i%2==0]
print c(1)
print c(1,2,)

c = lambda x: 'hello world'
print c('')

c = lambda : 'hello world 2'
print c()

	
	