#!/bin/python
#__encoding=utf-8__
import sys
import copy
import random


def zip2(*args):
    size = 0;
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
        yield tuple(paramArray)
        paramArray = []
    return


if __name__ == "__main__":
    print("----------- python version -----------")
    print(sys.version)
    print("----------- orginal test start -----------")
    seq = [1, 2, 3, 4, 5]
    seq2 = [10, 20, 30, 40, 50]
    seq3 = [100, 200, 300, 400, 500]
    print(zip(seq, seq2))
    print(zip(seq, seq2, seq3))
    print("----------- orginal test end -----------")
    print("----------- new code test start -----------")
    print(type(zip2(seq, seq2)))

    for i in zip2(seq, seq2):
        print(i)

    for i in zip2(seq, seq2, seq3):
        print(i)
    print("----------- new code test end -----------")
