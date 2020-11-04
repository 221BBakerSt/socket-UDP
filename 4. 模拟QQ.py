from threading import Thread
from socket import *
import time

def get_host_ip():
    # 获取本机IP

    try:
        s = socket(AF_INET, SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


def recvData():
    # 收数据并打印显示

    udpSocket = socket(type = SOCK_DGRAM)
    # Set an address this program will be bound to
    recvAddr = (get_host_ip(), my_port)
    udpSocket.bind(recvAddr)

    while 1:
        recvInfo = udpSocket.recvfrom(1024)
        recvMsg, (ip, port) = recvInfo
        recvMsg = recvMsg.decode('gb2312')
        print(f'>>[{time.ctime()}] {ip}:{port}: {recvMsg}\n')


def sendData():
    # 发数据并打印显示

    udpSocket = socket(type = SOCK_DGRAM)
    # Set an address the message will be sent to
    sendAddr = (your_ip, your_port)

    while 1:
        sendInfo = input('')
        print(f'<<[{time.ctime()}] 192.168.0.19:3310: {sendInfo}\n')
        sendInfo = sendInfo.encode('utf-8')
        udpSocket.sendto(sendInfo, sendAddr)


def main():
    global my_port, your_ip, your_port

    my_port = int(input('Please enter a port you want to take: '))
    your_ip = input("Please enter your friend's IP address: ")
    your_port = int(input("Please enter the port of your friend's program: "))

    print('Start chatting!')

    recv = Thread(target = recvData)
    send = Thread(target = sendData)

    recv.start()
    send.start()

    recv.join()
    send.join()

if __name__ == '__main__':
    main()
