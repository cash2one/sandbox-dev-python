#!/usr/bin/env python
#coding:utf-8

def zip2(arg,*args):
    
    a = list(args)
    a.insert(0,arg)
    for i in range(len(arg)):
        b =[]
        [ b.append(a[index2][i]) for index2 in range(len(a))]
        yield tuple(b)
   


l = [1,2,3,4]
ll = [5,6,7,8]
lll = [8,9,10,11]
#print zip2(l, ll) # -->  [(1, 5), (2, 6), (3, 7), (4, 8)]
#print zip2(l,ll,lll) #--> [(1, 5, 8), (2, 6, 9), (3, 7, 10), (4, 8, 11)]
print zip(l, ll, lll)
print zip2(l, ll, lll) #--> [(1, 5, 8, ...), (2, 6, 9, ...), (3, 7, 10, ...), (4, 8, 11, ...)]

for i in zip2(l, ll,lll):
    print i,
