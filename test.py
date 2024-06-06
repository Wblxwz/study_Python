import array
import copy
import weakref
import struct
import abc
from functools import singledispatch
from concurrent import futures

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
        """生成器函数"""
        yield self.x
        yield self.y
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

def fibo():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a + b

def coroutine():
    print('start...')
    x = yield 100
    print('recived:',x)

def threadFunc(num):
    print('thread',num)

if (__name__ == '__main__'):
    """myTuple = MyTuple(0,1)
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
    iter1 = iter(myTuple)
    print(next(iter1),next(iter1))
    try:
        print(iter(son))
    except TypeError:
        print(666)
    it = iter(fibo())
    print(next(it))
    print(next(it))
#可迭代的对象一定不能是自身的迭代器。也就是说，可迭代的对象必须实现__iter__方法，但不能实现__next__方法。
#另一方面，迭代器应该一直可以迭代。迭代器的__iter__方法应该返回自身。
    #生成器对象()
    #协程需要预激，即先next到yield位置
    cor = coroutine()
    print(next(cor))
    cor.send(10)
#    cor.throw(BaseException)
    next(cor)
Python线程受GIL(全局解释器锁)的限制，任何时候都只允许运行一个线程，但是GIL几乎对I/O密集型处理无害
CPython 解释器本身就不是线程安全的，因此有全局解释器锁（GIL），一次只允许使用一个线程执行 Python 字节码。因此，一个 Python 进程通常不能同时使用多个 CPU 核心。
Python 标准库中的所有阻塞型 I/O 函数都会释放 GIL，允许其他线程运行。time.sleep() 函数也会释放 GIL。因此，尽管有GIL，Python 线程还是能在 I/O 密集型应用中发挥作用。
使用 ProcessPoolExecutor 类把工作分配给多个Python 进程处理。因此，如果需要做 CPU 密集型处理，使用这个模块能绕开 GIL，利用所有可用的 CPU 核心。对CPU 密集型的处理来说，不可能要求使用超过 CPU 数量的职程。
Executor.map 函数返回结果的顺序与调用开始的顺序一致。如果第一个调用生成结果用时 10 秒，而其他调用只用 1 秒，代码会阻塞 10 秒，获取 map 方法返回的生成器产出的第一个结果。在此之后，获取后续结果时不会阻塞，因为后续的调用已经结束。
如果必须等到获取所有结果后再处理，这种行为没问题；不过，通常更可取的方式是，不管提交的顺序，只要有结果就获取。为此，要把Executor.submit 方法和 futures.as_completed 函数结合起来使用"""
    nums = (1,2,3,4,5)
    """with futures.ThreadPoolExecutor(5) as tp:
        tp.map(threadFunc,nums)
    #Process的参数大多数情况下不使用——默认值是os.cpu_count() 函数返回的 CPU 数量。
    with futures.ProcessPoolExecutor() as pp:
        pp.map(threadFunc,nums)"""
    my_futures = []
    with futures.ThreadPoolExecutor(3) as ftp:
        for num in nums:
            future = ftp.submit(threadFunc,num)
            my_futures.append(future)
        results = []
        for future in futures.as_completed(my_futures):
            res = future.result()
            results.append(res)