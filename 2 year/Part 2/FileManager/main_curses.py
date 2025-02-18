# main_curses.py
import curses
import os
from file_manager import FileManager
from config import load_config


def draw_status_bar(stdscr, fm, width):
    total, used, free = fm.get_disk_quota()
    status = f" Dir: {fm.get_current_directory()} | Disk: Total: {total // (1024 * 1024)}MB, Used: {used // (1024 * 1024)}MB, Free: {free // (1024 * 1024)}MB | 'q' – quit | 'b' – back "
    stdscr.attron(curses.color_pair(2))
    stdscr.addstr(0, 0, status.ljust(width))
    stdscr.attroff(curses.color_pair(2))


def draw_file_list(stdscr, fm, cursor_pos, height, width):
    try:
        files = fm.list_directory()
    except Exception as e:
        files = [f"Error: {e}"]
    for idx, item in enumerate(files):
        if idx + 2 >= height:
            break  # не выводим за пределы окна
        if idx == cursor_pos:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(idx + 2, 0, item.ljust(width))
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(idx + 2, 0, item.ljust(width))
    return files


def view_file_content(stdscr, fm, filename):
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    try:
        content = fm.read_file(filename)
    except Exception as e:
        content = f"Error reading file: {e}"
    lines = content.splitlines()
    stdscr.addstr(0, 0, f"File: {filename} - Press any key to return", curses.A_BOLD)
    for idx, line in enumerate(lines):
        if idx + 2 >= height:
            break
        stdscr.addstr(idx + 2, 0, line[:width - 1])
    stdscr.refresh()
    stdscr.getch()


def main(stdscr):
    curses.curs_set(0)  # скрыть курсор
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    # Определяем цветовые пары
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_YELLOW)  # выделение (курсор)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)  # статус-бар

    working_directory = load_config()
    fm = FileManager(working_directory)

    cursor_pos = 0

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        draw_status_bar(stdscr, fm, width)
        files = draw_file_list(stdscr, fm, cursor_pos, height, width)
        stdscr.refresh()

        key = stdscr.getch()
        if key == ord('q'):
            break
        elif key == curses.KEY_UP:
            cursor_pos = max(0, cursor_pos - 1)
        elif key == curses.KEY_DOWN:
            cursor_pos = min(len(files) - 1, cursor_pos + 1)
        elif key in [10, 13]:  # Enter
            if not files:
                continue
            selected = files[cursor_pos]
            abs_path = os.path.join(fm.get_current_directory(), selected)
            if os.path.isdir(abs_path):
                try:
                    fm.change_directory(selected)
                    cursor_pos = 0
                except Exception as e:
                    # Вывести ошибку в статус-баре
                    stdscr.addstr(height - 1, 0, f"Error: {e}", curses.color_pair(2))
                    stdscr.getch()
            else:
                view_file_content(stdscr, fm, selected)
        elif key == ord('b'):
            # Переход на уровень выше, если это разрешено
            parent = os.path.dirname(fm.get_current_directory())
            if parent.startswith(fm.working_directory):
                fm.change_directory("..")
                cursor_pos = 0


curses.wrapper(main)
