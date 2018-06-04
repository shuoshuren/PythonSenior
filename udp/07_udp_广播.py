import socket,sys

dest = ("<broadcast>",7788)

#创建udp套接字
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#对要发送广播数据打套接字进行设置
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

# 以广播的形式发送数据到本网络打所有电脑
s.sendto("Hi",dest)

print("等待回复.....")

while True:
	(buf,address) = s.recvfrom(2048)
	print("received from %s:%s" %(address,buf))
