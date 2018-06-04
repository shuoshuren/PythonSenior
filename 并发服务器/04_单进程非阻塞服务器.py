from socket import *

#1.创建套接字
serSocket = socket(AF_INET,SOCK_STREAM)

#重复使用绑定信息
serSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

# 绑定本地ip和port
localAddr = ('',7788)
serSocket.bind(localAddr)

# 让这个socket变为非阻塞
serSocket.setblocking(False)

#3.将socket变为监听套接字
serSocket.listen(5)

# 用来保存所有已经连接打客户端的信息
clientAddrList = []

while True:


	# 等待客户端到来
	try:
		clientSocket,clientAddr = serSocket.accept()
	except:
		pass
	else:
		print("-----新的客户端到来：%s----"%str(destAddr))
        clientSocket.setblocking(False)
        clientAddrList.append((clientSocket,clientAddr))

    for clientSocket,clientAddr in clientAddrList:
        try:
            recvData = clientSocket.recv(1024)
        except:
            pass
        else:
            if len(recvData) > 0:
                print("[%s]:%s" %(str(clientAddr),recvData))
            else:
                clientSocket.close()
                clientAddrList.remove((clientSocket,clientAddr))
                print("%s 已经下线"%(str(clientAddr)))
	


serSocket.close()



