import socket
from threading import Thread

class Receiver(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.running = True
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind(("0.0.0.0",5000))
        
    def run(self):
        while self.running:
            dati, indirizzo_client = self.s.recvfrom(4096)
            print(f"{dati.decode()}")

    def stop(self):
        self.running = False

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ricevo = Receiver()
    ricevo.start()
    while True:
        stringa = input("Messaggio:")
        nome = input("Nome: ")
        msg = stringa + "|" + nome
        s.sendto(msg.encode(), ("192.168.0.136", 5000))
        
        if(stringa == "Exit") | (stringa == "exit"):
            ricevo.stop()
            ricevo.join()
            break
    
        
if __name__ =="__main__":
    main()