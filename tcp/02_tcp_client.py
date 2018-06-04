from socket import *


clientSocket = socket(AF_INET,SOCK_STREAM)

clientSocket.connect(("192.168.119.3",8899))

# tcp 客户端链接好了服务器，所以在以后的数据发送中不需要填写对方打ip和port

clientSocket.send("haha".encode("utf8"))

recvData = clientSocket.recv(1024)

print("recvData:%s" %recvData)

clientSocket.close()