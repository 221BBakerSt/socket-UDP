from socket import *
import time

def main(port, num):
    udpSocket = socket(type = SOCK_DGRAM)
    print('UDP socket created')
    # bind the address
    udpSocket.bind(('', port))
    for _ in range(num):
        recvData = udpSocket.recvfrom(1024)
        msg, (ip, port) = recvData
        msg = msg.decode('gb2312')
        print(f'[{time.ctime()}] {ip}:{port}: {msg}')

if __name__ == '__main__':
    main(3201, 10)
