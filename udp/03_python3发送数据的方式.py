from socket import *


ip = input("请输入要发送的ip:")
port = int(input("请输入要发送的端口:"))
data = input("请输入要发送的数据:")

udpSocket = socket(AF_INET,SOCK_DGRAM)

udpSocket.sendto(data.encode("gb2312"),(ip,port))