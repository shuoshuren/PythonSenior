#!/usr/bin/python
# coding=utf-8

from socket import *
from multiprocessing import Process
import re

# 设置静态文件根目录
HTML_ROOT_DIR = "./html/"


def handle_client(client_socket):
    '''处理客户端请求'''
    # 接收数据
    request_data = client_socket.recv(1024)
    print("request data:", request_data)

    # 解析HTTP 数据
    request_lines = request_data.splitlines()
    # for line in request_lines:
    # print(line)

    # 提取请求方式
    # 提取请求路径path
    # 'GET / HTTP/1.1'
    request_start_line = request_lines[0]
    print("*" * 20)
    print(request_start_line.decode("utf-8"))
    file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_line.decode("utf-8")).group(1)

    if "/" == file_name:
        file_name = "/index.html"

    # 打开文件，读取内容
    try:
        file = open(HTML_ROOT_DIR + file_name, "rb")
    except IOError:
        response_start_line = "HTTP/1.1 404 Not Found\r\n"
        response_headers = "Server: My Server\r\n"
        response_body = "The file is not found"
    else:
        file_data = file.read()
        file.close()

        # 构造响应数据
        response_start_line = "HTTP/1.1 200 OK\r\n"
        response_headers = "Server: My Server\r\n"
        response_body = file_data.decode("utf-8")

    response = response_start_line + response_headers + '\r\n' + response_body
    print("response data:", response)

    # 返回请求数据
    client_socket.send(bytes(response, "utf-8"))
    # 关闭客户端连接
    client_socket.close()


if __name__ == '__main__':

    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind(('', 8000))
    server_socket.listen(5)

    while True:
        client_socket, client_address = server_socket.accept()
        print("[%s,%s]用户连接上" % client_address)
        handle_client_process = Process(
            target=handle_client, args=(client_socket,))
        handle_client_process.start()
        client_socket.close()
