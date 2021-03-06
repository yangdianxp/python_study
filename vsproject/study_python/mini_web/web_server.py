import sys
import socket
import re
import multiprocessing
import time
#import dynamic.mini_frame

class WSGIServer(object):
    def __init__(self, port, app, static_path):
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.tcp_server_socket.bind(("", port))
        self.tcp_server_socket.listen(128)

        self.application = app
        self.static_path = static_path

    def service_client(self, new_socket):
        request = new_socket.recv(1024).decode("utf-8")
        #print(request)
        request_lines = request.splitlines()
        print(request_lines)
        if not request_lines:
            new_socket.close()
            return
        ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
        file_name = ""
        if ret:
            file_name = ret.group(1)
            if file_name == "/":
                file_name = "/index.html"
        print("file_name:{}".format(file_name))

        if not file_name.endswith(".html"):
            try:
                f = open(self.static_path + file_name, "rb")
            except Exception as result:
                print(result)
                response = "HTTP/1.1 404 NOT FOUND\r\n"
                response += "\r\n"
                response += "------file not found-----"
                new_socket.send(response.encode("utf-8"))
            else:
                html_content = f.read()
                f.close()
                response = "HTTP/1.1 200 OK\r\n"
                response += "\r\n"
                new_socket.send(response.encode("utf-8"))
                new_socket.send(html_content)
        else:
            env = dict()
            env['PATH_INFO'] = file_name 
            body = self.application(env, self.set_response_header)

            header = "HTTP/1.1 {}\r\n".format(self.status)
            for temp in self.headers:
                header += "{}:{}\r\n".format(temp[0], temp[1])
            header += "\r\n"
            response = header + body
            new_socket.send(response.encode("utf-8"))
    
        new_socket.close()

    def set_response_header(self, status, headers):
        self.status = status
        self.headers = [("server", "mini_web v8.8")]
        self.headers += headers

    def run_forever(self):
        while True:
            new_socket, client_addr = self.tcp_server_socket.accept()
            print("client_addr:{}".format(client_addr))
            p = multiprocessing.Process(target=self.service_client, args=(new_socket,))
            p.start()
            new_socket.close()
        self.tcp_server_socket.close()

def main():
    if len(sys.argv) == 3:
        port = int(sys.argv[1])
        frame_app_name = sys.argv[2]
    else:
        print("请按照以下方式运行:")
        print("python3 xxxx.py 7890 mini_frame:application")
        return

    ret = re.match(r"([^:]+):(.*)", frame_app_name)
    if ret:
        frame_name = ret.group(1)
        app_name = ret.group(2)
    else:
        print("请按照以下方式运行:")
        print("python3 xxxx.py 7890 mini_frame:application")
        return

    with open("./mini_web/web_server.conf") as f:
        conf_info = eval(f.read())
    # 此时conf_info是一个字典

    sys.path.append(conf_info["dynamic_path"])
    frame = __import__(frame_name)  # 返回值标记着导入的这个模块
    app = getattr(frame, app_name)

    wsgi_server = WSGIServer(port, app, conf_info["static_path"])
    wsgi_server.run_forever()
        
if __name__ == "__main__":
    try:
        main()
    except:
        ex_type, ex_val, ex_stack = sys.exc_info()
        print(ex_type)
        print(ex_val)
        for stack in traceback.extract_tb(ex_stack):
            print(stack)
