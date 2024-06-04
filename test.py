import array
import copy
import weakref
import struct
import abc
from functools import singledispatch

def deco(func):
    """装饰器"""
    j = 10
    print("deco...")
    def deco2(*args):
        nonlocal j
        j += 5
        print(args,j)
        return func(*args)
    return deco2

@deco
def ceShi(a,b):
    return a

def cs(s):
    print(id(s))
    s.append(4)
    print(id(s))
    return s

class MyTuple:

    __pri = 10
    __att = 20
    @property
    def pri(self):
        return self.__pri

    def __getattr__(self, item):
        print(item)
        return self.__att

    def __add__(self, other):
        return MyTuple(self.x + other.x,self.y + other.y)

    def __radd__(self, other):
        return self + other

    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __iter__(self):
        return (i for i in (self.x,self.y))
    def __repr__(self):
        return '{!r},{!r}'.format(*self)
    def __bytes__(self):
        return bytes([ord('i')]) + bytes(array.array('i',self))
    #__slots__ = ('x','y')
    def __del__(self):
        print('del...')
    def __len__(self):
        return 2
    def __format__(self, format_spec):
        return '{!r},{!r}'.format(self.x,self.y)
    @classmethod
    def ces(*args):
        print(args)

def bye():
    print('Bye~')
class Parent(abc.ABC):
    @abc.abstractmethod
    def a(self):
        pass
    def b(self):
        return 100
class Son(Parent):
    def a(self):
        return 1
    def __init__(self):
        self.s = '1'
    @staticmethod
    def c():
        return 11
@singledispatch
def single(a):
    print(a)
@single.register(int)
def single1(a):
    print('int',a)
@single.register(str)
def single1(a):
    print('str',a)
if (__name__ == '__main__'):
    myTuple = MyTuple(0,1)
    # print(struct.pack('<I',1))
    # print(bytes(myTuple))
    s = '{name:0.2f}'
    print(s.format(name=0.44444))

    list1 = [1,2,3,4,5]
    t = type(myTuple)
    tt = t(2,3)
    print(tt.__att)
    tt.abc = 55
    #Parent.register(Son)
    print(issubclass(Son,Parent))
    son = Son()
    print(Son.a(son))
    print(Son.__mro__)
    print(myTuple + tt)
    single(1)
    single('123')