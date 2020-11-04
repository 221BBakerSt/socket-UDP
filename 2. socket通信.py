from socket import *
# 创建TCP socket

tcpSocket = socket(AF_INET, SOCK_STREAM)
print('TCP socket created')
# 设置地址，端口和要发送的数据
sendAddr = ('192.168.0.19', 3306)
# 如果此处没写b，下面使用sendData时要变成sendData.encode('utf-8')
sendData = b'ok, tcp'
# 连接服务器和发送
# tcpSocket.connect(sendAddr)
# tcpSocket.send(sendData)
# 关闭socket
tcpSocket.close()

##############################################
# 创建UDP socket
udpSocket = socket(AF_INET, SOCK_DGRAM)
print('UDP socket created')

# 绑定本地信息，如果一个网络程序不稳定，系统就会随机分配。但一般情况作为接收方时需要绑定
# bind()参数是个元祖 #IP一般不用写，表示本机任何一个IP，有几个网卡就几个IP
udpSocket.bind(('', 3304))

# 设置地址，端口和要发送的数据
sendAddr = ('192.168.0.19', 3306)
sendData = 'ok, 尼玛123'
# 在这里就他妈的提前转换好编码
sendData = sendData.encode('utf-8')
# 连接服务器和发送
udpSocket.sendto(sendData, sendAddr)

# 等待接收方发送数据
# 设置一次只接收1024 bytes
recvdata = udpSocket.recvfrom(1024)
# recvData是个元祖
content, host_info = recvdata
# 如果接收的是中文消息，用utf-8解码会报错的！
content = content.decode('gb2312')
print(content, host_info)

# 关闭socket
udpSocket.close()
