import socket

def send_file_2_client(new_client_socket, client_addr):
    file_name = new_client_socket.recv(1024).decode("utf-8")
    print("客户端({})需要下载文件是：{}".format(client_addr, file_name))
    file_content = None
    try:
        f = open(file_name, 'rb')
        file_content = f.read()
        f.close()
    except Exception as ret:
        print(ret)
    #new_client_socket.send("dfkjasldfjsfjasdf ".encode('utf-8'))
    if file_content:
        new_client_socket.send(file_content)


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(("", 7890))
    tcp_server_socket.listen(128)

    while True:
        new_client_socket, client_addr = tcp_server_socket.accept()
        print(client_addr)

        send_file_2_client(new_client_socket, client_addr)
        new_client_socket.close()
    
    tcp_server_socket.close()

if __name__ == "__main__":
    main()
