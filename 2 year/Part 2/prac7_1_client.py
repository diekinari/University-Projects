import socket

def start_client():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 9090))
    except Exception as e:
        print("Ошибка подключения к серверу:", e)
        return

    try:
        while True:
            message = input("Введите сообщение (или 'exit' для выхода): ")
            if message.lower() == "exit":
                print("Завершение работы клиента.")
                break

            try:
                client_socket.sendall(message.encode('utf-8'))
            except Exception as e:
                print("Ошибка при отправке сообщения:", e)
                break

            try:
                response = client_socket.recv(1024)
                if not response:
                    print("Сервер закрыл соединение.")
                    break
                print(f"Ответ от сервера: {response.decode('utf-8')}")
            except Exception as e:
                print("Ошибка при получении ответа от сервера:", e)
                break

    except Exception as e:
        print("Ошибка во время работы клиента:", e)
    finally:
        client_socket.close()

start_client()
