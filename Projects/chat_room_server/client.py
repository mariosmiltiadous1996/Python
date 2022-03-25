import socket
import threading
import time 
tLock = threading.Lock()
shutdown = False

def receving(name, sock):
    while not shutdown:
        try:
            tLock.acquire()
            while True:
                data, addr = sock.recvfrom(1024)
                print str(data)
        except:
            pass
        finally:
            tLock.release()

host = raw_input("dwse_hostIp:")
ports= input("dwse_port:")#port to server oxi tou client!!!!!!!!!
while not  0<ports<65536 :
    print ("mono metaksi 0-65535")
    ports= input("dwse_port:")
server = (host,ports)
port=0
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

rT = threading.Thread(target=receving, args=("RecvThread",s))
rT.start()

name = raw_input("Onoma: ")
message = raw_input(name + "-> ")
while message != 'q':
    if message != '':
        s.sendto(name + ": " + message, server)
    tLock.acquire()
    message = raw_input(name + "-> ")
    tLock.release()
    time.sleep(0.1)

shudown = True
rT.join()
s.close()

