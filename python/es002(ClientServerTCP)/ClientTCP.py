import socket
from threading import Thread

class Reciver(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.running = True
    
    def run(self):
        while self.running:
            msgR = s.recv(4096)
            print(msgR.decode())
            
    def stop(self):
        self.running = False

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.0.112",8000))

r = Reciver()
r.start()

while True:
    msgS = input("Inserisci un messaggio> ")
    s.sendall(msgS.encode())
    

s.close()