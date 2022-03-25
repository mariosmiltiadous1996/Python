import socket
import time

host = '127.0.0.1'
port= int(input("dwse_port:"))
while port<0 or port >65535 :
    print ("mono metaksi 0-65535")
    port= int(input("dwse_port:"))
           

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

quitting = False
print "Server Started."
while not quitting:
    try:
        data, addr = s.recvfrom(1024)
        if "Quit" in str(data):
            quitting = True
        if addr not in clients:
            clients.append(addr)
            
        print time.ctime(time.time()) + str(addr) + ": :" + str(data)
        for client in clients:
            
            s.sendto(data, client)
    except:
        pass

s.close()

