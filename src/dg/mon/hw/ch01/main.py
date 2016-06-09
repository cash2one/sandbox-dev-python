#!/bin/python
#__encoding=utf-8__


import sys
import copy
import random


def pascals_triangle1(n):
    x = [[1]]
    for i in range(n - 1):
        x.append([sum(i) for i in zip([0] + x[-1], x[-1] + [0])])
    return x


def pascals_triangle2(n):
    x = [[1]]
    for i in range(n - 1):
        x.append(list(map(sum, zip([0] + x[-1], x[-1] + [0]))))
    return x


pascals_triangle3 = lambda n: [[i for i in str(11 ** j)] for j in range(n)]


def create_fibonacci(n):
    pascals_result = pascals_triangle1(n)
    print("pascals result is:")
    for i in pascals_result:
        print i
    print("fibnacci is:")
    allfib = []
    for i in range(1, n + 1):
        m = 0
        fib = 0
        while m <= i - 1 - m:
            cursor = pascals_result[i - 1 - m][m]
            fib = fib + cursor
            m = m + 1
        allfib.append(fib)

    workArr = []
    for i in range(n):
        print pascals_result[i]
        tempArr = copy.copy(pascals_result[i])
        tempArr.append(allfib[i])
        workArr.append(tempArr)
    print("The Result is:")
    for i in workArr:
        print i
    print("The End.")


def printHeart():
    printData = []
    rowData = "    ***        ";
    printData.append(rowData + " " + rowData[::-1])
    rowData = " *********     ";
    printData.append(rowData + " " + rowData[::-1])
    rowData = "************   ";
    printData.append(rowData + " " + rowData[::-1])
    rowData = "*************  ";
    printData.append(rowData + " " + rowData[::-1])
    rowData = "************** ";
    printData.append(rowData + " " + rowData[::-1])
    rowData = "***************";
    printData.append(rowData + " " + rowData[::-1])
    rowData = " ********   ***";
    printData.append(rowData + " " + rowData[::-1])
    rowData = "  *******    **";
    printData.append(rowData + "*" + rowData[::-1])
    rowData = "   *******    *";
    printData.append(rowData + "*" + rowData[::-1])
    rowData = "     ******    ";
    printData.append(rowData + "*" + rowData[::-1])
    rowData = "       ******  ";
    printData.append(rowData + "*" + rowData[::-1])
    rowData = "          *****";
    printData.append(rowData + "*" + rowData[::-1])
    rowData = "           ****";
    printData.append(rowData + "*" + rowData[::-1])
    rowData = "            ***";
    printData.append(rowData + "*" + rowData[::-1])
    rowData = "             **";
    printData.append(rowData + "*" + rowData[::-1])
    rowData = "              *";
    printData.append(rowData + "*" + rowData[::-1])
    rowData = "               ";
    printData.append(rowData + "*" + rowData[::-1])
    printData.append(rowData + rowData[::-1])
    for i in printData: print("   " + i)


if __name__ == "__main__":
    while (True):
        inputStr = sys.stdin.readline()
        if inputStr == "1\n":
            inputNum = random.randrange(1, 15)
            create_fibonacci(inputNum)
        elif inputStr == "2\n":
            printHeart()
        elif inputStr == "3\n":
            break
