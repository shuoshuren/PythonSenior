from socket import *

udpSocket = socket(AF_INET,SOCK_DGRAM)

# udp 发送数据，在每一次的时候都需要写上接收方的ip和port
udpSocket.sendto(b"haha",("193.168.0.102",8080))
