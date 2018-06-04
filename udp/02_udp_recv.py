from socket import *

# 1.创建套接字
udpSocket = socket(AF_INET,SOCK_DGRAM)

# 2.绑定本地的相关信息，如果不绑定，系统会随机分配
bindAddr = ("",7080)# ip地址和端口，IP一般不写，表示本机的任何一个ip
udpSocket.bind(bindAddr)

#3.等待接收方发送数据
recvData = udpSocket.recvfrom(1024) #1024表示本次接受的最大字节数

#4. 显示接收到的数据
print(recvData)

#5.关闭套接字
udpSocket.close()
