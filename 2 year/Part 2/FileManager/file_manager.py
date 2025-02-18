# file_manager.py
import os
import shutil

class FileManager:
    def __init__(self, working_directory):
        # Рабочая директория задается один раз, и все операции ограничены этим пространством
        self.working_directory = os.path.abspath(working_directory)
        self.current_directory = self.working_directory

    def _get_absolute_path(self, path):
        # Формирует абсолютный путь относительно текущей директории
        abs_path = os.path.abspath(os.path.join(self.current_directory, path))
        # Проверяем, что абсолютный путь начинается с пути рабочей директории
        if not abs_path.startswith(self.working_directory):
            raise Exception("Access denied: попытка доступа за пределы рабочей директории.")
        return abs_path

    def list_directory(self):
        return os.listdir(self.current_directory)

    def change_directory(self, path):
        new_path = self._get_absolute_path(path)
        if os.path.isdir(new_path):
            self.current_directory = new_path
        else:
            raise Exception("Указанная директория не существует.")

    def make_directory(self, dirname):
        path = self._get_absolute_path(dirname)
        os.makedirs(path, exist_ok=True)
        return path

    def remove_directory(self, dirname):
        path = self._get_absolute_path(dirname)
        # Для удаления используем os.rmdir (удаляет только пустые директории)
        os.rmdir(path)
        return path

    def create_file(self, filename, content=""):
        path = self._get_absolute_path(filename)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return path

    def read_file(self, filename):
        path = self._get_absolute_path(filename)
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    def write_file(self, filename, content):
        path = self._get_absolute_path(filename)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return path

    def delete_file(self, filename):
        path = self._get_absolute_path(filename)
        os.remove(path)
        return path

    def copy_file(self, source, destination):
        source_path = self._get_absolute_path(source)
        destination_path = self._get_absolute_path(destination)
        shutil.copy2(source_path, destination_path)
        return destination_path

    def move_file(self, source, destination):
        source_path = self._get_absolute_path(source)
        destination_path = self._get_absolute_path(destination)
        shutil.move(source_path, destination_path)
        return destination_path

    def rename_file(self, source, new_name):
        source_path = self._get_absolute_path(source)
        destination_path = os.path.join(os.path.dirname(source_path), new_name)
        # Проверяем, что новый путь остается внутри рабочей директории
        if not destination_path.startswith(self.working_directory):
            raise Exception("Access denied: нельзя переименовать файл за пределами рабочей директории.")
        os.rename(source_path, destination_path)
        return destination_path

    def get_current_directory(self):
        return self.current_directory
