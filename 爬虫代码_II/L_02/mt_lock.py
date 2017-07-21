import threading
from multiprocessing import cpu_count

balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()
    print(balance)


if __name__ == '__main__':
    threads = []
    for i in range(cpu_count()):
        t = threading.Thread(target=run_thread, args=(500, ))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()