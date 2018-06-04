# coding:utf-8

import time
# from MyWebServer import HttpServer


# 设置静态文件根目录
HTML_ROOT_DIR = "./html/"


class Application(object):
    """框架的核心部分"""

    def __init__(self, urls):
        # 设置路由信息
        self.urls = urls

    def __call__(self, env, start_response):
        path = env.get("PATH_INFO", "/")
        # /static/ 开头就是静态文件
        if path.startswith("/static"):
            # 要访问打静态文件
            file_name = path[7:]
            # 打开文件，读取内容
            try:
                file = open(HTML_ROOT_DIR + file_name, "rb")
            except IOError:
                # 未找到路由信息，404错误
                status = "404 Not Found"
                headers = []
                start_response(status, headers)
                return "not found"
            else:
                file_data = file.read()
                file.close()

                # 构造响应数据
                status = "200 OK"
                headers = [
                    ("Server","MyServer")
                ]
                start_response(status, headers)
                return file_data.decode("utf-8")

        for url, handler in self.urls:
            if path == url:
                return handler(env, start_response)

        # 未找到路由信息，404错误
        status = "404 Not Found"
        headers = []
        start_response(status, headers)
        return "not found"


def show_ctime(env, start_response):
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    start_response(status, headers)
    return time.ctime()


def say_hello(env, start_response):
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    start_response(status, headers)
    return "Hello Client"


urls = [
        ("/", show_ctime),
        ("/ctime", show_ctime),
        ("/sayhello", say_hello)
]

app = Application(urls)

# if __name__ == '__main__':
#     urls = [
#         ("/", show_ctime),
#         ("/ctime", show_ctime),
#         ("/sayhello", say_hello)
#     ]
#
#     app = Application(urls)
#
#     http_server = HttpServer(app)
#     http_server.bind(8000)
#     http_server.start()
