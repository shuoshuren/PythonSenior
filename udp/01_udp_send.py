from socket import *

udpSocket = socket(AF_INET,SOCK_DGRAM)

# udp �������ݣ���ÿһ�ε�ʱ����Ҫд�Ͻ��շ���ip��port
udpSocket.sendto(b"haha",("193.168.0.102",8080))
