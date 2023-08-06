import socket
import threading

host = socket.gethostbyname(socket.gethostname())
port = 5000
client_conns = []

s = socket.socket()
s.bind((host, port))
s.listen(10)

print(s.family, s.type)


def broadcast_msg(msg, current_conn):
    for conn in client_conns:
        if conn != current_conn:
            conn.send(msg.encode())

def handle_client(conn):
    while True:
        msg = conn.recv(4096).decode()
        broadcast_msg(msg, conn)
        

while True:
    conn, address = s.accept()
    print(f"Connection from: {address}")
    client_conns.append(conn)

    threading.Thread(target=handle_client, args=[conn]).start() 
    #threading._start_new_thread(handle_client, (conn,))
