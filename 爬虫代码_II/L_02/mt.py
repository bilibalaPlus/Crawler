import threading

def func(v_1, v_2):
    print(threading.current_thread().name, ':', v_1, v_2)

t = threading.Thread(target=func, name='t1', args=('hello', 'world'))
t.start()
t.join()