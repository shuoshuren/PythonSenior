from socket import *
import select




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


#创建一个epoll对象
epoll = select.epoll()

#注册事件到epoll,EPOLLIN:可读，EPOOLLOUT:可写，
#EPOLLET(edge trigger):当epoll检测到描述事件发生并将事件通知应用程序，程序应该立即处理
#EPOLLLT(level trigger):当epoll检测到描述事件发生并将事件通知应用程序,应用程序可以不立即处理，下次调用epoll
epoll.register(s.fileno(),select.EPOLLIN|select.EPOLLET)


connections = {}
addresses = {}



while running:

	#epoll 进行fd扫描打地方，未指定超时时间为阻塞等待
	epoll_list = epoll.poll()

	# 对事件进行判断
	for fd,events in epoll_list:

		#监听到有新的连接
		if fd == serSocket.fileno():
			
			conn,addr = serSocket.accept()
			
			print("-------新的客户端到来：%s------"%(str(addr)))

			#将conn,addr保存起来
			connections[conn.fileno()] = conn
			addresses[conn.fileno()] = addr

			#向epoll中注册连接socket的可读事件
			epoll.register(conn.fileno(),select.EPOLLIN|select.EPOLLET)


		# 判断事件是否是接收数据打事件
		elif events == select.EPOLLIN:
			# 从激活fd上接收
			clientAddr,data = connections[fd].recv(1024)
			if len(data) > 0:
                print("[%s]:%s" %(str(clientAddr),data))
                sock.send(data)
            else:
            	#从epoll中移除fd
            	epoll.unregister(fd)

            	#server 侧主动关闭socket
            	connections[fd].close()

            	print("----%s--offline-------"%str(connections[fd]))
                

		#有数据到来
		else:
			
	


serSocket.close()



