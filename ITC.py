#线程间通信
import multiprocessing
import threading
import time

buffer = []
buffer_size = 5

notEmpty = threading.Condition()
notFull = threading.Condition()

def producer():
    for i in range(10):
        #上下文管理器 自动拿锁退锁
        with notFull:
            while len(buffer) >= buffer_size:
                notFull.wait()
            buffer.append(i)
            with notEmpty:
                notEmpty.notify()
def consumer():
    while True:
        with notEmpty:
            while len(buffer) == 0:
                notEmpty.wait()
            print(buffer.pop(0))
            with notFull:
                notFull.notify()

#该队列为线程安全的
queue = multiprocessing.Queue()

def producer1():
     for i in range(10):
         queue.put(i)
def consumer1():
    while True:
        print(queue.get())
if __name__ == "__main__":
    t1 = threading.Thread(target=producer1)
    t2 = threading.Thread(target=consumer1)

    threads = []
    threads.append(t1)
    threads.append(t2)

    for t in threads:
        t.start()
    for t in threads:
        t.join()