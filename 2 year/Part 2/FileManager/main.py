# main.py
import sys
from file_manager import FileManager
from config import load_config
from colorama import init, Fore, Style

# Инициализация colorama (на Windows это нужно для корректного вывода ANSI последовательностей)
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
    print(Fore.CYAN + "  help                           - показать справку")
    print(Fore.CYAN + "  exit                           - выйти из файлового менеджера")

def main():
    working_directory = load_config()
    fm = FileManager(working_directory)
    print(Fore.LIGHTGREEN_EX + "Добро пожаловать в файловый менеджер на Python!")
    print(Fore.LIGHTGREEN_EX + "Рабочая директория: " + fm.get_current_directory())
    print("Введите 'help' для просмотра доступных команд.")

    while True:
        try:
            # Красим приглашение в зелёный цвет
            command_input = input(Fore.LIGHTGREEN_EX + f"{fm.get_current_directory()}> " + Style.RESET_ALL).strip()
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
