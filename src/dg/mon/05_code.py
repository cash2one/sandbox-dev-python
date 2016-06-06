#!/usr/bin/python
'''file description ...'''


def count():
    i = 2
    def f(j):
        return j**i
    return f

f1 = count()
print f1.__closure__
print f1(2)


def count():
    i = 2
    def f(j, i=i):
        return j**i
    return f

f1 = count()
print f1.__closure__  #None
print f1(2)


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print (f1(), f2(), f3())   ##   9, 9, 9


f1, f2, f3 = [lambda:i*i for i in range(1, 4)]   ##列表解析表达式充当匿名函数
print i
print f1(), f2() ,f3()   #  9,9,9
i = 5
print i
print f1(), f2() ,f3()   # 25,25,25
del i
print f1(), f2() ,f3()   #  NameError: global name 'i' is not defined


def make_adder(addend):
    def adder(augend):
        return augend + addend
    return adder
	
add23 = make_adder(23)
add44 = make_adder(44)

print add23(100)  #   100+23=123
print add44(100)  #    100+44=144


def add100(f):
    def adder():
        return f() + 100
    return adder

@ add100
def f():
    return 5

print f()  #  105


def add100(f):
    def adder(x):   ##接收f的参数
        return f(x) + 100
    return adder

@ add100   #  f = add100(f)
def f(x):
        return x

print f(5)   # 105


def addn(n):      #  接收 装饰器 参数
    def make_adder(f):  #   接收 被装饰 函数
        def adder(x):  #   接收 函数 参数
            return f(x) + n
        return adder
    return make_adder

@addn(200)  # f = addn(200)(f)
def f(x):
    return x

print f(55)  # 255


'''装饰器调用顺序'''
def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makebold    #   依次调用
@makeitalic  #   优先调用
def hello():
    return "hello world"

print hello()  #  <b><i>hello world</i></b>


'''类装饰器'''
class function_wrapper(object):
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        return self.f(*args, **kwargs)

@function_wrapper  ##-> f = function_wrapper(f)
def f():
    pass

print f
print dir(f)


'''装饰器模板'''
from decorator import decorator

@decorator
def f_warpper(f, x):
    return x**2

@f_warpper
def f(x):
    return x

print f(5)


'''Log 应用'''
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print '%s() was called...' % func.__name__
        return func(*args, **kw)
    return wrapper

@log
def now():
    print '2016-04-21'

now()
print now.__name__



	
	