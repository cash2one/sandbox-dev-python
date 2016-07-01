def map2(func, *arglist):
    l=zip(*arglist)
    rest=[func(*x) for x in l]
    return rest
f = lambda x: x ** 2
f2 = lambda x,y: x * y
seq = [1, 2, 3, 4, 5]
seq2 = [10, 20, 30, 40, 50]
t1=map2(f,seq)
t2=map2(f2, seq,seq2)
print t1
print t2
输出
[1, 4, 9, 16, 25]
[10, 40, 90, 160, 250]