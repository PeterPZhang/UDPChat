import socket

# 接收消息功能函数
def recv_msg(udp_socket):
    # 接收数据 1024:每次接收数据的最大字节数
    recv_data, ip_port = udp_socket.recvfrom(1024)
    # 解码数据
    recv_content = recv_data.decode("gbk")
    print(recv_content, ip_port)

# 发送消息功能函数
def send_msg(udp_socket):
    # 接收用户发送的数据
    send_content = input("请输入您要发送的数据:")
    # 使用gbk进行编码
    send_data = send_content.encode("gbk")
    # 接收对方的ip和端口
    dest_ip = input("请输入对方的ip地址:")
    port = int(input("请输入对方的端口号:"))
    # 发送数据
    udp_socket.sendto(send_data, (dest_ip, port))


if __name__ == '__main__':
    # 创建udpsocket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定端口
    udp_socket.bind(("", 9090))
    while True:
        # 接收用户输入的选项
        option = input("请输入功能选项 1.发送 2.接收 3.退出:")
        if option == "1":
            # # 接收用户发送的数据
            # send_content = input("请输入您要发送的数据:")
            # # 使用gbk进行编码
            # send_data = send_content.encode("gbk")
            # # 接收对方的ip和端口
            # dest_ip = input("请输入对方的ip地址:")
            # port = int(input("请输入对方的端口号:"))
            # # 发送数据
            # udp_socket.sendto(send_data, (dest_ip, port))
            send_msg(udp_socket)
        elif option == "2":
            # 接收数据 1024:每次接收数据的最大字节数
            # recv_data, ip_port = udp_socket.recvfrom(1024)
            # # 解码数据
            # recv_content = recv_data.decode("gbk")
            # print(recv_content, ip_port)
            recv_msg(udp_socket)
        elif option == "3":
            break

    # 关闭socket
    udp_socket.close()
def zorozhang_test():
    print("hello my friend!!!")
    # 提示：在同一台电脑上不能使用相同的端口号，在同一台电脑上端口号是唯一的