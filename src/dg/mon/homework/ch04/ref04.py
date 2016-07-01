#!/usr/bin/python
# encoding:utf-8
__author__="Yu"

def zip2(*args):
    len1=len(args) #遍历所有的参数，找出最小长度的参数,按最小长度的数组进行遍历并组合成行的元组，列表
    lmin=len(args[0])
    for length in range(len1):
        if lmin > len(args[length]):
            lmin=len(args[length])
    for i in range(lmin):
        ss="("
        for j in range(len(args)):
            if j<len(args)-1:
                ss=ss+str(args[j][i])+","
            else:
                ss=ss+str(args[j][i])
        ss=ss+")"
        #print ss
        yield eval(ss)
        #l.append(eval(ss))
    #print l

def p(f):
    print f
    for i in f:
        print i

l = [1,2,3,4]
ll = [5,6,7,8]
lll = [8,9,10,11]
f=zip2(l, ll)
f1=zip2(l,ll,lll)
p(f)
p(f1)

t=[1,2,3,4]
tt=[2,3,4]
ttt=[1,4]
#print zip(t,tt,ttt)
fun=zip2(t,tt,ttt)
p(fun)
