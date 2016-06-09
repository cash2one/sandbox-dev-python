#!/bin/python
#__encoding=utf-8__
import sys
import copy
import random

def map2(func, *args):
    size =0;
    paramArray = []
    resultArray = []
    if len(args):
        size = len(args[0])
        for arg in args:
            if len(arg) != size:
                return
    else:
        return

    for i in range(size):
        for j in range(len(args)):
            paramArray.append(args[j][i])
        resultArray.append(func(*paramArray))
        paramArray=[]
    return resultArray

if __name__=="__main__":
    print("-----------orginal test start-----------")
    f = lambda x: x ** 2
    seq = [1, 2, 3, 4, 5]
    m = map(f, seq)
    # [1, 4, 9, 16, 25]
    print(m)
    f2 = lambda x,y: x * y
    seq = [1, 2, 3, 4, 5]
    seq2 = [10, 20, 30, 40, 50]
    m = map(f2, seq, seq2)
    # [10, 40, 90, 160, 250]
    print(m)
    print("-----------orginal test end-----------")
    print("-----------new code test start-----------")
    print("map2's result is : " + str(map2(f, [])))
    print("map2's result is : " + str(map2(f, seq)))
    print("map2's result is : " + str(map2(f2, seq, seq2)))
    print("-----------new code test end-----------")
