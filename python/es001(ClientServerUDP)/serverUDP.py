from posixpath import split
import socket

f = open("rubrica.csv", 'r')
righe = f.readlines()
dizionario = {}


for riga in righe[1:]:
    rigaSplittata = riga[:-1].split(',')
    dizionario[rigaSplittata[0]] = rigaSplittata[1]

print(dizionario)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 5001))

while True:
    dati, indirizzo_client = s.recvfrom(4096)
    print(f"{dati} ricevuti da {indirizzo_client}")
    dato = dati.decode()
    temp = dato.split('|')
    
    print(f"{temp[0]} inviato a {temp[1]}")
    s.sendto(temp[0].encode(), (dizionario[temp[1]], 5001))