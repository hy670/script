import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(2)
try:
    s.connect(('192.168.0.1',81))
    print ("端口开启")
except:
    print ("端口关闭")

s.close()