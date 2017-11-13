#``````````````````````````````````````````````````````````````````````````````````````````````````````#!/usr/bin/python3 


####### Import functions here 
from main import main

## End import

import socket, time         # Import socket module

s = socket.socket()         # Create a socket object
port = 8002             # Reserve a port for your service.
s.bind(("localhost", port))          # Bind to the port
s.listen(5)                 # Now wait for client connection.

print('Server is running on port {}'.format(port))

try:
    while True:
        c, addr = s.accept()                     # Establish connection with client.
        print('Got connection from', addr)

        while True:
            rawmsg = c.recv(1024)          # recieve up to 1024 bytes
            
            ## Keyword checking goes here (if statements)

                output= main(rawmsg)

                msg = output   # convert and clean the input
            
            ## End keyword checking
            
            rtrnmsg = msg.rstrip('\r\n')                    # create return message
            print( '%s -> %s' % (msg,rtrnmsg) )

            rtrnmsg = rtrnmsg 
            c.send( rtrnmsg.encode('utf-8') )    # send return message

        print('Disconnected')
        c.close()                                # Close the connection

except KeyboardInterrupt:                        # catch Ctrl-C signals so that we shutdown nicely
    pass

finally:                                        # make certain that the sockets get closed properly
    print('Shutdown')
    s.shutdown(1)
    s.close()
