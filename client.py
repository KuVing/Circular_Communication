# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 14:45:45 2021

@author: Administrator
"""

import socket
def main():
    tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_ip="192.168.70.1"
    server_port = 8999
    server_add=(server_ip,server_port)
    tcp_server_socket.connect(server_add)
    first_data=tcp_server_socket.recv(1024)
    print(first_data.decode("utf-8"))
    while True:
        send_data=input("send-->")
        tcp_server_socket.send(send_data.encode("UTF-8"))
    tcp_server_socket.close()

if __name__=="__main__":
    main()                                       