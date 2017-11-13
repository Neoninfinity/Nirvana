#!/usr/bin/python3 
import socket

client = socket.socket()
port = 8002
client.connect(('localhost', port))

try:
    while True:
        msg = input('>')
        client.send( msg.encode('utf-8') )
        data = client.recv(1024)
        data = data.decode("utf-8")
        print(data)
        

except KeyboardInterrupt:
    print('Shutdown')
    client.shutdown(1)
    client.close()
