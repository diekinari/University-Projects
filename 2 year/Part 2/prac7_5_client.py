import socket

def udp_client(message="standart message"):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = ('localhost', 9090)

    client_socket.sendto(message.encode(), server_address)
    if message == "exit":
        print("Завершение работы клиента.")
        return

    response, _ = client_socket.recvfrom(1024)
    print(f"Ответ от сервера: {response.decode()}")

    client_socket.close()

while True:
    message = input("Введите сообщение (или 'exit' для выхода): ")
    if message.lower() == "exit":
        udp_client(message)
        break
    udp_client(message)
