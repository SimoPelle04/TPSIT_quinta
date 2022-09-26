import socket
from threading import Thread

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

class receive(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.running = True
    
    def run(self):
        while self.running:
            msg, ind_client = s.recvfrom(4096)
            print("Server>" + msg.decode())

    def stop(self):
        self.running = False

s.bind(("192.168.0.124",8000))
s.listen()

print("In attesa di connessione...")
connection, address = s.accept()
connection.sendall("Ti sei connesso".encode())
print(address)
while True:
    msgS = input("Inserisci un messaggio> ")
    connection.sendall(msgS.encode())
    msgR = connection.recv(4096)
    print(msgR.decode())

    if msgS == "exit":
        break

s.close()