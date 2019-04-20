import socket
import re
import select

def service_client(new_socket, request):
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

    try:
        f = open("html" + file_name, "rb")
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

def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(("", 7890))
    tcp_server_socket.listen(128)

    epl = select.epoll()
    epl.register(tcp_server_socket.fileno(), select.EPOLLIN)

    fd_event_dict = dict()
    while True:
        fd_event_list = epl.poll()
        for fd, event in fd_event_list:
            if fd == tcp_server_socket.fileno():
                new_socket, client_addr = tcp_server_socket.accept()
                print("client_addr:{}".format(client_addr))
                epl.register(new_socket.fileno(), select.EPOLLIN)
                fd_event_dict[new_socket.fileno()] = new_socket
            elif event == select.EPOLLIN:
                recv_data = fd_event_dict[fd].recv(1024).decode("utf-8")
                if recv_data:
                    service_client(fd_event_dict[fd], recv_data)
                else:
                    print("client close")
                    fd_event_dict[fd].close()
                    epl.unregister(fd)
                    del fd_event_dict[fd]


if __name__ == "__main__":
    main()