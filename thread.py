from time import sleep

import threading
import multiprocessing

def test1():
    print("test1...")

def test2():
    print("test2...")

#t1 = threading.Thread(target=test1)
#t2 = threading.Thread(target=test2)

"""多进程"""
pipe = multiprocessing.Pipe()

def pipe1(pipe):
    pipe.send("11111")
    print("recv",pipe.recv())
def pipe2(pipe):
    pipe.send("22222")
    print("recv",pipe.recv())
t1 = multiprocessing.Process(target=pipe1,args=(pipe[0],))
t2 = multiprocessing.Process(target=pipe2,args=(pipe[1],))

threads = []

threads.append(t1)
threads.append(t2)


'''join()方法通常应用在以下场景中：
让主线程在子线程完成之后再继续执行，保证线程的顺序性。
在多个子线程并发执行任务的情况下，需要等待所有子线程完成后再统一处理结果。
协调多个线程之间的执行顺序，保证某些操作的原子性和同步性，在这种情况下，你可以使用 join() 方法来控制线程的运行顺序。'''
if __name__ == "__main__":
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("end...")