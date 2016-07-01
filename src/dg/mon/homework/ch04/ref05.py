# -*- coding: utf-8 -*- a = [-i for i in range(1, 16) if i % 3 == 1]
b = [i for i in range(1, 16) if i % 3 == 2]
c = [i for i in range(1, 16) if i % 3 == 0] print "输出a:", a print "输出b:", b print "输出c:", c def map2(*seq):
    lislen = len(seq) '''判断传入参数是否是空'''  if lislen == 0: print "Don't input None list!"  exit() # print "Wrong exit!---1"  seqlen = len(seq[0]) '''判断各list长度是否相等'''  for i in range(lislen - 1): if len(seq[i]) != len(seq[i + 1]): print "wrong input, every parameter'lenth have to be equal!"  exit() # print "Wrong exit!---2"   output = [] for j in range(seqlen):
        tmp = [] for i in range(lislen):
            tmp.append(seq[i][j])
        output.append(tmp) yield output
zip=map2(a) for i in range(5): print zip.next()

zip=map2(a,b) for i in range(5): print zip.next()

zip=map2(a,b,c) for i in range(5): print zip.next()