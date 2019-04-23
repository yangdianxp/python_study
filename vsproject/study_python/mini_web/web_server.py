import socket
import re
import multiprocessing
import time

class WSGIServer(object):
    def __init__(self):
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.tcp_server_socket.bind(("", 7890))
        self.tcp_server_socket.listen(128)

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

        if not file_name.endswith(".py"):
            try:
                f = open("web_server/html" + file_name, "rb")
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
            header = "HTTP/1.1 200 OK\r\n"
            header += "\r\n"
            body = "hahaha {}".format(time.ctime())
            response = header + body
            new_socket.send(response.encode("utf-8"))
    
        new_socket.close()

    def run_forever(self):
        while True:
            new_socket, client_addr = self.tcp_server_socket.accept()
            print("client_addr:{}".format(client_addr))
            p = multiprocessing.Process(target=self.service_client, args=(new_socket,))
            p.start()
            new_socket.close()
        self.tcp_server_socket.close()

def main():
    wsgi_server = WSGIServer()
    wsgi_server.run_forever()
        
if __name__ == "__main__":
    main()