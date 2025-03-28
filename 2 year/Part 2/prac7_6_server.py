import selectors
import socket

selector = selectors.DefaultSelector()

def accept_connection(server_socket):
    client_socket, client_address = server_socket.accept()
    print(f"Подключение от {client_address}")
    selector.register(client_socket, selectors.EVENT_READ, send_echo)

def send_echo(client_socket):
    data = client_socket.recv(1024)
    if data:
        try:
            client_socket.sendall(data)
        except Exception as e:
            selector.unregister(client_socket)
            client_socket.close()
            print(e)


    elif data.decode() == "shutdown":
        selector.unregister(client_socket)
        client_socket.close()
        print("Сервер завершил работу.")
    else:
        selector.unregister(client_socket)
        client_socket.close()


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9090))
    server_socket.listen()
    server_socket.setblocking(False)
    selector.register(server_socket, selectors.EVENT_READ, accept_connection)

    print("Сервер запущен и ожидает подключений...")
    while True:
        events = selector.select(timeout=None)
        print(events)

        for key, _ in events:
            callback = key.data
            callback(key.fileobj)

start_server()