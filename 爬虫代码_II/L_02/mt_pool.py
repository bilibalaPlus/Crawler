import grequests

def run_thread(v):
    if v % 5 == 0:
        print('value = ' + str(v))

if __name__ == '__main__':
    requests = threadpool.makeRequests(run_thread, [i for i in range(500)])
    pool = threadpool.ThreadPool(cpu_count())
    [pool.putRequest(req) for req in requests]
    pool.wait()
