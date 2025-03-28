import socket

def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 9090))

    print("UDP сервер запущен и ожидает сообщений...")
    while True:
        message, client_address = server_socket.recvfrom(1024)
        if message.decode() == 'exit':
            print("Сервер завершил работу.")
            break
        print(f"Получено сообщение от {client_address}: {message.decode()}")
        server_socket.sendto(message, client_address)

    server_socket.close()

udp_server()