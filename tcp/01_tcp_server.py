from socket import *


serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.bind(("",8899))

serverSocket.listen(5)

# clientSocket:表示这个新的客户端
# clientInfo:表示这个新打客户端打ip以及port
clientSocket,clientInfo = serverSocket.accept()

recvData = clientSocket.recv(1024)

print("%s:%s"%(str(clientInfo),recvData))

clientSocket.close()
serverSocket.close()
