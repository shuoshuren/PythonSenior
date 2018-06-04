from socket import *
from threading import Thread


def dealWithClient(newSocket,destAddr):

	while True:
		recvData = newSocket.recvData(1024)
		if len(recvData) > 0:
			print("recv[%s]:%s" %(str(destAddr),recvData))
		else:
			print("[%s]客户端已经关闭"%str(destAddr))
			break
		
	newSocket.close()



def main():

	serSocket = socket(AF_INET,SOCK_STREAM)

	#重复使用绑定信息
	serSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

	localAddr = ('',7788)

	serSocket.bind(localAddr)

	serSocket.listen(5)

	try:

		while True:

			print("----------主进程，等待客户端到来-----------")

			newSocket,destAddr = serSocket.accept()

			print("--------------主进程，创建一新进程来进行数据处理--·[%s]----"%str(destAddr))

			client = Thread(target=dealWithClient,args=(newSocket,destAddr))
			client.start()

			# 线程中共享了这个套接字，如果关闭会导致套接字不可用
			# newSocket.close()
			
			
	finally:
		#当所有客户端服务完了之后，在进行关闭，表示不再接受新的客户端链接
		serSocket.close()



if __name__ == '__main__':
	main()
