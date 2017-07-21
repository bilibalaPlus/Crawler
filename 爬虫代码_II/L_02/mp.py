import os
from multiprocessing import Process

def run_proc(v_1, v_2):
    print('Run child process %s %s (%s)...' % (v_1, v_2, os.getpid()))

if __name__ == '__main__':
    p = Process(target=run_proc, args=('hello', 'world'))
    print('Start child process.')
    p.start()
    p.join()
    print('Child process end.')