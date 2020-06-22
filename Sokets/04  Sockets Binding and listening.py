import socket
import sys

host = ''
port = 5555

# Creatina socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host,port))
except socket.error as e:
    print(str(e))

s.listen(5)

conn,addr = s.accept()

print('connected: ' +addr[0]+':'+str(addr[1]))
