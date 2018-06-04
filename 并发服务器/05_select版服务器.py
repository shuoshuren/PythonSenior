from socket import *
import select
import sys

#select 缺点： 个数存在限制，采用轮询的方法效率低,不管socket是否是活跃的，都会遍历一遍，会浪费cpu时间


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

inputs = [serSocket,sys.stdin]

running = True

while running:

	#select函数，阻塞等待
	readable,writeable,exceptional = select.select(inputs,[],[])

	# 在select去检测inputs这个列表中的时候，所检测出来打所有可以进行接受数据打套接字
	for sock in readable:

		#监听到有新的连接
		if sock == serSocket:
			conn,addr = serSocket.accept()
			#select监听的socket
			inputs.append(conn)

		# 监听到键盘输入
		elif sock == sys.stdin:
			cmd = sys.stdin.readline()
			running = False
			break

		#有数据到来
		else:
			clientAddr,data = sock.recv(1024)
			if len(data) > 0:
                print("[%s]:%s" %(str(clientAddr),data))
                sock.send(data)
            else:
            	#移除select监听打socket
                inputs.remove(sock)
                sock.close()
	


serSocket.close()



