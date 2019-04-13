import socket

def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    local_addr = ('', 7788)
    udp_socket.bind(local_addr)
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)
        recv_msg = recv_data[0]
        print(recv_msg.decode('gbk'))
    udp_socket.close()

#def main():
#    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#    udp_socket.sendto(b"haha", ("192.168.1.52", 8080))
#    udp_socket.close()
if __name__ == "__main__":
    main()
