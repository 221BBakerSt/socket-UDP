from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)
udpSocket.bind(('', 69))

f = open('/Users/allen/Desktop/wan-copy.py', 'wb')
while udpSocket.recvfrom(1024):
    recvData = udpSocket.recvfrom(1024)
    f.write(recvData)
f.close()
udpSocket.close()
