import os
from multiprocessing import Process
from multiprocessing import Queue

def run_proc(q):
    while not q.empty():
        v = q.get(True)
        print('Run child process %s (%s)...' % (v, os.getpid()))

if __name__ == '__main__':
    q = Queue()
    for i in range(100):
        q.put(i)
    p_1 = Process(target=run_proc, args=(q, ))
    p_2 = Process(target=run_proc, args=(q, ))
    print('Start')
    p_1.start()
    p_2.start()
    p_1.join()
    p_2.join()
    print('End')