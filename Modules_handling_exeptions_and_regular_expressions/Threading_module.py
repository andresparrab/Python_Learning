import threading
from queue import Queue
import time

print_lock = threading.Lock()

def worker(job):
    time.sleep(0.5)
    with print_lock:
        print(threading.current_thread().name,'Task'+str(job))

def  worker_thread():
    while True:
        job = q.get()
        worker(job)
        q.task_done()

q= Queue()
num_jobs=20
num_workers=10

for wk in range(num_workers):
    t = threading.Thread(target = worker_thread)
    t.name = 'Worker-'+str(wk)
    t.daemon = True
    t.start()

start = time.time()

for job in range(num_jobs):
    q.put(job)

q.join()

print('Entyre job took: ',time.time()-start)