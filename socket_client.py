import socket
import threading

host = socket.gethostbyname(socket.gethostname())
port = 5000

s = socket.socket()
s.connect((host, port))

def recieve():
    data = s.recv(4096).decode()
    print(data)

alias = input("Alias: ")
#threading.Thread(target=recieve).start()

while True:
    message = input(f"{alias}: ")
    message = alias + ": " + message
    s.send(message.encode())

    data = s.recv(4096).decode()
    print(data)
        

