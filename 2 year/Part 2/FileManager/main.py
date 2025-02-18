# main.py
import sys
import os
from file_manager import FileManager
from config import load_config
from user_manager import login_user, register_user
from colorama import init, Fore, Style

# Инициализация colorama для корректного вывода ANSI-последовательностей (особенно на Windows)
init(autoreset=True)


def print_help():
    print(Fore.CYAN + "Доступные команды:")
    print(Fore.CYAN + "  ls                             - вывести список файлов и папок в текущей директории")
    print(Fore.CYAN + "  cd <path>                      - сменить текущую директорию")
    print(Fore.CYAN + "  mkdir <dirname>                - создать новую директорию")
    print(Fore.CYAN + "  rmdir <dirname>                - удалить пустую директорию")
    print(Fore.CYAN + "  create <filename> [content]    - создать файл с необязательным содержимым")
    print(Fore.CYAN + "  read <filename>                - прочитать содержимое файла")
    print(Fore.CYAN + "  write <filename> <content>     - записать содержимое в файл (перезаписать)")
    print(Fore.CYAN + "  delete <filename>              - удалить файл")
    print(Fore.CYAN + "  copy <source> <destination>    - скопировать файл")
    print(Fore.CYAN + "  move <source> <destination>    - переместить файл")
    print(Fore.CYAN + "  rename <source> <new_name>     - переименовать файл")
    print(Fore.CYAN + "  archive <source> <archive>     - архивировать файл/директорию в zip-архив")
    print(Fore.CYAN + "  unarchive <archive> <dest>     - разархивировать zip-архив в указанную директорию")
    print(Fore.CYAN + "  quota                          - показать информацию о дисковом пространстве")
    print(Fore.CYAN + "  help                           - показать справку")
    print(Fore.CYAN + "  exit                           - выйти из файлового менеджера")


def user_auth(base_directory):
    print(Fore.MAGENTA + "Добро пожаловать в многопользовательский файловый менеджер!")
    print(Fore.MAGENTA + "Выберите действие:")
    print(Fore.MAGENTA + "  1. Войти")
    print(Fore.MAGENTA + "  2. Зарегистрироваться")
    choice = input("Введите 1 или 2: ").strip()
    if choice == "1":
        username = login_user(base_directory)
    elif choice == "2":
        username = register_user(base_directory)
    else:
        print(Fore.RED + "Неверный выбор.")
        return None
    return username


def main():
    # Загружаем базовую рабочую директорию из конфигурации
    base_directory = load_config()

    # Получаем имя пользователя через систему авторизации
    username = None
    while username is None:
        username = user_auth(base_directory)

    # Персональная директория пользователя будет находиться в base_directory/users/<username>
    user_dir = os.path.join(base_directory, "users", username)
    print(Fore.GREEN + f"Рабочая директория пользователя: {user_dir}")

    # Создаем экземпляр файлового менеджера с персональной директорией пользователя
    fm = FileManager(user_dir)

    print(Fore.GREEN + "Добро пожаловать в файловый менеджер на Python!")
    print("Введите 'help' для просмотра доступных команд.")

    while True:
        try:
            # Вычисляем относительный путь для приглашения
            rel_path = os.path.relpath(fm.get_current_directory(), fm.working_directory)
            prompt_path = "~ " if rel_path == "." else "~/" + rel_path

            # Вывод приглашения (prompt) окрашен зелёным
            command_input = input(Fore.LIGHTGREEN_EX + f"{prompt_path}> " + Style.RESET_ALL).strip()
            if not command_input:
                continue

            parts = command_input.split()
            cmd = parts[0].lower()
            args = parts[1:]

            if cmd == "ls":
                items = fm.list_directory()
                for item in items:
                    print(Fore.MAGENTA + item)
            elif cmd == "cd":
                if len(args) != 1:
                    print(Fore.RED + "Использование: cd <путь>")
                else:
                    fm.change_directory(args[0])
            elif cmd == "mkdir":
                if len(args) != 1:
                    print(Fore.RED + "Использование: mkdir <имя_папки>")
                else:
                    fm.make_directory(args[0])
                    print(Fore.LIGHTGREEN_EX + "Директория создана.")
            elif cmd == "rmdir":
                if len(args) != 1:
                    print(Fore.RED + "Использование: rmdir <имя_папки>")
                else:
                    fm.remove_directory(args[0])
                    print(Fore.LIGHTGREEN_EX + "Директория удалена.")
            elif cmd == "create":
                if len(args) < 1:
                    print(Fore.RED + "Использование: create <имя_файла> [содержимое]")
                else:
                    filename = args[0]
                    content = " ".join(args[1:]) if len(args) > 1 else ""
                    fm.create_file(filename, content)
                    print(Fore.LIGHTGREEN_EX + "Файл создан.")
            elif cmd == "read":
                if len(args) != 1:
                    print(Fore.RED + "Использование: read <имя_файла>")
                else:
                    content = fm.read_file(args[0])
                    print(Fore.MAGENTA + content)
            elif cmd == "write":
                if len(args) < 2:
                    print(Fore.RED + "Использование: write <имя_файла> <содержимое>")
                else:
                    filename = args[0]
                    content = " ".join(args[1:])
                    fm.write_file(filename, content)
                    print(Fore.LIGHTGREEN_EX + "Файл записан.")
            elif cmd == "delete":
                if len(args) != 1:
                    print(Fore.RED + "Использование: delete <имя_файла>")
                else:
                    fm.delete_file(args[0])
                    print(Fore.LIGHTGREEN_EX + "Файл удалён.")
            elif cmd == "copy":
                if len(args) != 2:
                    print(Fore.RED + "Использование: copy <источник> <назначение>")
                else:
                    fm.copy_file(args[0], args[1])
                    print(Fore.LIGHTGREEN_EX + "Файл скопирован.")
            elif cmd == "move":
                if len(args) != 2:
                    print(Fore.RED + "Использование: move <источник> <назначение>")
                else:
                    fm.move_file(args[0], args[1])
                    print(Fore.LIGHTGREEN_EX + "Файл перемещён.")
            elif cmd == "rename":
                if len(args) != 2:
                    print(Fore.RED + "Использование: rename <источник> <новое_имя>")
                else:
                    fm.rename_file(args[0], args[1])
                    print(Fore.LIGHTGREEN_EX + "Файл переименован.")
            elif cmd == "archive":
                if len(args) != 2:
                    print(Fore.RED + "Использование: archive <источник> <архив>")
                else:
                    fm.archive_file(args[0], args[1])
                    print(Fore.LIGHTGREEN_EX + "Архив создан.")
            elif cmd == "unarchive":
                if len(args) != 2:
                    print(Fore.RED + "Использование: unarchive <архив> <директория>")
                else:
                    fm.unarchive_file(args[0], args[1])
                    print(Fore.LIGHTGREEN_EX + "Архив разархивирован.")
            elif cmd == "quota":
                total, used, free = fm.get_disk_quota()
                print(
                    Fore.MAGENTA + f"Диск: Всего: {total // (1024 * 1024)}MB, Использовано: {used // (1024 * 1024)}MB, Свободно: {free // (1024 * 1024)}MB")
            elif cmd == "help":
                print_help()
            elif cmd == "exit":
                print(Fore.MAGENTA + "Выход из файлового менеджера.")
                break
            else:
                print(Fore.RED + "Неизвестная команда. Введите 'help' для просмотра команд.")
        except Exception as e:
            print(Fore.RED + "Ошибка: " + str(e))


if __name__ == "__main__":
    main()
