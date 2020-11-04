from socket import *
import sys

dest = ('<broadcast>', 8080)

# Create the socket
s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

# send it to the exchanger
s.sendto('Hi', dest)

print('waiting for the response...')

while 1:
    (buf, address) = s.recvfrom(2048)
    print(f'Received from {address}: {buf}')
