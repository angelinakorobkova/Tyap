import socket
conn = socket.socket()
port = 8080
addr = "127.0.0.1"
conn.connect((addr,port))
print(conn.recv(1024).decode())

b = input('Введите команду time" ')
conn.send(b.encode())
print(conn.recv(65565).decode())
conn.close()