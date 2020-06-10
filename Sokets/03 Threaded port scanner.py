import socket
import threading
from queue import Queue

print_lock = threading.Lock()
q = Queue()
target = 'pythonprogramming.net'

# Scan the port and see if its open or not. If it can connect or not
def port_scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target,port))
        with print_lock:
            print('port', port, 'is open !!!')
        con.close()
    except:
        pass

# what to do with each thread
def threader():
    while True:
        port = q.get()
        port_scan(port)
        q.task_done()

# then number of threads to run simuntanously
for thread in range(300):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()


#run trhough ports from 1 to 10000
for port in range(1,10000):
    q.put(port)

q.join()
