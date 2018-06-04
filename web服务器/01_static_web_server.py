#!/usr/bin/python
#coding:utf-8

from socket import *
from multiprocessing import Process


HTML_ROOT_DIR = "./html/"


def handle_client(client_socket):
	'''处理客户端请求'''
	# 接收数据
	request_data = client_socket.recv(1024)
	print("request data:",request_data)
	# 解析HTTP 数据
	# 提取请求方式
	# 提取请求路径path

	# 构造响应数据
	response_start_line = "HTTP/1.1 200 OK\r\n"
	response_headers = "Server: My Server\r\n"
	response_body = "hello client"
	response = response_start_line+ response_headers+'\r\n'+response_body
	print("response data:",response)
	# 返回请求数据
	client_socket.send(bytes(response,"utf-8"))
	# 关闭客户端连接
	client_socket.close()


if __name__ == '__main__':

	server_socket = socket(AF_INET,SOCK_STREAM)
	server_socket.bind(('',8000))
	server_socket.listen(5)


	while True:
		client_socket,client_address = server_socket.accept()
		print("[%s,%s]用户连接上"%client_address)
		handle_client_process = Process(target=handle_client,args=(client_socket,))
		handle_client_process.start()
		client_socket.close()





