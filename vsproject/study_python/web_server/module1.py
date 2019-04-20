import socket

def service_client(new_socket):
    request = new_socket.recv(1024)
    print(request)
    response = "HTTP/1.1 200 OK\r\n"
    response += "\r\n"
    response += "<h1>hahaha</h1>"
    new_socket.send(response.encode("utf-8"))
    new_socket.close()

def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(("", 7890))
    tcp_server_socket.listen(128)
    while True:
        new_socket, client_addr = tcp_server_socket.accept()
        print("client_addr:{}".format(client_addr))
        service_client(new_socket)
        
if __name__ == "__main__":
    main()