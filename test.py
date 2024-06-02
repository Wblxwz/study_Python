
import copy
import weakref

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
def ceShi(a):
    return a

def cs(s):
    print(id(s))
    s.append(4)
    print(id(s))
    return s

class BB:
    a = None

class AA:
    b = BB

def bye():
    print('Bye~')
if (__name__ == '__main__'):
    a = AA
    b = BB
    b.a = a
    weak_a = weakref.finalize(a,bye)
    weak_b = weakref.finalize(b,bye)
    print()
