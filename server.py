# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 14:44:49 2021

@author: 15003
"""

import socket
def main():
    tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #等价于socket.socket
    tcp_server_socket.bind(("",8999)) #允许多人链接我
    tcp_server_socket.listen(128)
    while True:
        new_client_socket,client_addr=tcp_server_socket.accept()
        print("the %s is connnecting "%(str(client_addr)))
        new_client_socket.send("Welcome".encode("UTF-8"))
        while True:
            try:
                recv_deta=new_client_socket.recv(1024)
                print(recv_deta.decode("UTF-8"))
            except:
                print("断开连接")
                break
        new_client_socket.close()
    tcp_server_socket.close()
if __name__=="__main__":
    main()     
            
        
    