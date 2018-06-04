#!/usr/bin/python
# coding=utf-8

from socket import *
from multiprocessing import Process
import re
import sys

# 设置静态文件根目录
HTML_ROOT_DIR = "./html/"
WSGI_PYTHON_DIR = "./wsgipython"


class HttpServer(object):
    """"""

    def __init__(self,application):
        """构造函数，application 指的是框架的app"""
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.app = application

    def bind(self, port):
        self.server_socket.bind(('', port))

    def start(self):
        self.server_socket.listen(128)
        while True:
            client_socket, client_address = self.server_socket.accept()
            print("[%s,%s]用户连接上" % client_address)
            handle_client_process = Process(
                target=self.handle_client, args=(client_socket,))
            handle_client_process.start()
            client_socket.close()

    def start_response(self, status, headers):
        server_headers = [
            ("Server", "My Server")
        ]
        response_headers = "HTTP/1.1 " + status + "\r\n"
        for header in headers:
            response_headers += "%s: %s\r\n" % header
        self.response_headers = response_headers

    def handle_client(self, client_socket):
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
        method = re.match(r"(\w)+ +/[^ ]* ", request_start_line.decode("utf-8")).group(1)
        print("file_name:%s" % file_name)
        # /ctime.py

        env = {
            "PATH_INFO":file_name,
            "METHOD":method
        }
        response_body = self.app(env, self.start_response)
        response = self.response_headers + "\r\n" + response_body

        print("response data:", response)

        # 返回请求数据
        client_socket.send(bytes(response, "utf-8"))
        # 关闭客户端连接
        client_socket.close()


def main():

    sys.path.insert(1, WSGI_PYTHON_DIR)

    if len(sys.argv)< 2:
        sys.exit("python MyWebServer.py Module:app")

    # python MyWebServer.py  MyWebFramework:Application
    module_name,app_name = sys.argv[1].split(":")
    m = __import__(module_name)
    # Application = getattr(m,app_name)
    # app = Application()
    # python MyWebServer.py  MyWebFramework:app
    app = getattr(m,app_name)

    http_server = HttpServer(app)
    http_server.bind(8000)
    http_server.start()


if __name__ == '__main__':
    main()
