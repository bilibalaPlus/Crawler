import threading

def func(v_1, v_2):
    for i in range(1,10):
        print(threading.current_thread().name, ':', v_1, v_2)

t = threading.Thread(target=func, name='t1', args=('hello', 'world'))
t1 =  threading.Thread(target=func, name='t2', args=('hi', 'world'))
t.start()
t.join()
t1.start()
t1.join()
print('after!!!!!!!!')