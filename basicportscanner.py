#!usr/bin/env python3

import socket               #socket module imported

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# I have created a socket variable.
# AF_INET is for the IPV4 Address and SOCK_STREAM is for the TCP OR UDP protocol

host = input("Please enter the ip : = ")
port = int(input("Please enter the port number := "))
# mentioned the target and the port

# creating the function portscanner
def portscanner(port):
    result = s.connect_ex((host,port))
    if result == 0:
        print("Port is opened")
    else:
        print("port is closed")

#calling the function portscanner
portscanner(port)





