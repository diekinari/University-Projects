import socket
import threading
import logging
import time

# Настройка логирования: логи будут записываться в файл server.log
logging.basicConfig(
    filename='server.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

# Глобальное событие для завершения работы сервера
shutdown_event = threading.Event()
# Список для хранения активных потоков клиентов
client_threads = []


def handle_client(client_socket, client_address):
    logging.info(f"Подключение от {client_address}")
    try:
        while not shutdown_event.is_set():
            try:
                data = client_socket.recv(1024)
                if not data:
                    logging.info(f"Клиент {client_address} разорвал соединение.")
                    break
                message = data.decode('utf-8').strip()
                logging.info(f"Сообщение от {client_address}: {message}")

                # Обработка специальной команды shutdown
                if message.lower() == 'shutdown':
                    logging.info("Получена команда shutdown. Инициирую завершение работы сервера.")
                    shutdown_event.set()
                    client_socket.sendall(b"Server is shutting down.")
                    break

                # Эхо-ответ: отправляем обратно полученное сообщение
                client_socket.sendall(data)
            except ConnectionResetError:
                logging.warning(f"Клиент {client_address} неожиданно разорвал соединение.")
                break
            except Exception as e:
                logging.error(f"Ошибка при обработке клиента {client_address}: {e}")
                break
    finally:
        client_socket.close()
        logging.info(f"Соединение с {client_address} закрыто.")


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Позволяет повторно использовать адрес без задержки после перезапуска
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 9090))
    server_socket.listen()
    logging.info("Сервер запущен и ожидает подключений...")
    print("Сервер запущен и ожидает подключений...")

    try:
        while not shutdown_event.is_set():
            try:
                # Устанавливаем таймаут для проверки shutdown_event
                server_socket.settimeout(1.0)
                client_socket, client_address = server_socket.accept()
                client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
                client_thread.start()
                client_threads.append(client_thread)
            except socket.timeout:
                continue  # Проверяем shutdown_event, если таймаут истек
            except Exception as e:
                logging.error(f"Ошибка при принятии соединения: {e}")
    finally:
        server_socket.close()
        logging.info("Сервер сокет закрыт.")
        print("Сервер сокет закрыт. Ожидание завершения активных соединений...")
        # Ожидаем завершения всех потоков клиентов
        for t in client_threads:
            t.join()
        logging.info("Сервер завершил работу.")
        print("Сервер завершил работу.")


if __name__ == '__main__':
    start_server()
