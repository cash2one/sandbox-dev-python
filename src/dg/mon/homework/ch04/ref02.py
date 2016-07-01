
#!/user/bin/python
# encoding:utf-8
import sys
import string

def zip2(*args):
    if len(args) == 0:
        print "There is no input parameters!"
    else:
        for arg in args:
            if type(arg) is not tuple and type(arg) is not list:
                print "Input parameter must be list or tuple!"
                return
        argLens = [len(arg) for arg in args]
        if len(set(argLens)) != 1:
            print "The paramenter list or tuple have different length!"
            return
        else:
            index = 0
            while index < len(args[0]):
                yieldvalue = [arg[index] for arg in args]
                yield tuple(yieldvalue)
                index = index + 1
            return

def main(argv):
    seq = [1, 2, 3, 4, 5]
    seq2 = [10, 20, 30, 40, 50]

    print "using zip fuction sequences"
    for m in zip(seq, seq2):
        print m

    print "using zip2 fuction sequences"
    zipitems = zip2(seq, seq2)
    for zipitem in zipitems:
        print zipitem

if __name__ == "__main__":
    main(sys.argv)

using zip fuction sequences
(1, 10)
(2, 20)
(3, 30)
(4, 40)
(5, 50)
using zip2 fuction sequences
(1, 10)
(2, 20)
(3, 30)
(4, 40)
(5, 50)