import socket
import logging
import time

logging.basicConfig(
    filename='server.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Позволяет повторно использовать адрес без задержки после перезапуска
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 9090))
    server_socket.listen()
    logging.info("Сервер запущен и ожидает подключений...")
    print("Сервер запущен и ожидает подключений...")

    shutdown = False

    try:
        while not shutdown:
            try:
                # Устанавливаем таймаут для возможности проверки флага shutdown
                server_socket.settimeout(1.0)
                client_socket, client_address = server_socket.accept()
            except socket.timeout:
                continue  # Если нет подключения, продолжаем цикл
            except Exception as e:
                logging.error(f"Ошибка при принятии соединения: {e}")
                continue

            logging.info(f"Подключение от {client_address}")
            print(f"Подключение от {client_address}")

            try:
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        logging.info(f"Клиент {client_address} разорвал соединение.")
                        break

                    message = data.decode('utf-8').strip()
                    logging.info(f"Сообщение от {client_address}: {message}")

                    # Если получена команда shutdown, завершаем работу сервера
                    if message.lower() == "shutdown":
                        shutdown = True
                        client_socket.sendall(b"Server is shutting down.")
                        logging.info("Получена команда shutdown. Завершаю работу сервера.")
                        break

                    # Эхо-ответ: отправляем обратно полученное сообщение
                    client_socket.sendall(data)
            except ConnectionResetError:
                logging.warning(f"Клиент {client_address} неожиданно разорвал соединение.")
            except Exception as e:
                logging.error(f"Ошибка при обработке клиента {client_address}: {e}")
            finally:
                client_socket.close()
                logging.info(f"Соединение с {client_address} закрыто.")
                print(f"Соединение с {client_address} закрыто.")
    finally:
        server_socket.close()
        logging.info("Серверный сокет закрыт.")
        print("Серверный сокет закрыт.")
        logging.info("Сервер завершил работу.")
        print("Сервер завершил работу.")

if __name__ == '__main__':
    start_server()
