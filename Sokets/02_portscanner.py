import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = 'pythonprogramming.net'

def p_scan(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False

for x in range(1,26):
    if p_scan(x):
        print('Port : ',x , 'is OPEN !!!')
    else:
        print('Port %d is closed'%(x))
