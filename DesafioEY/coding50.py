import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('158.69.192.239', 1337))

rec = s.recv(1024)
print(rec)

s.send(b'start')
rec = s.recv(1024)

while True:
    rec = s.recv(1024)
    print(rec)
    if b"EY" in rec:
        break;
    resposta = eval(rec)
    maior = str(max(resposta))
    s.send(bytes(maior, 'utf-8'))
