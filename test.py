
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

if (__name__ == '__main__'):
    print(ceShi(5))
