import os
from multiprocessing import Pool
from multiprocessing import Queue
from multiprocessing import cpu_count

def run_proc(v):
    if v % 5 == 0:
        print('Run child process %s (%s)...' % (v, os.getpid()))

if __name__ == '__main__':
    print(cpu_count())
    p = Pool(cpu_count())
    for i in range(500):
        p.apply_async(run_proc, args=(i, ))
    p.close()
    p.join()