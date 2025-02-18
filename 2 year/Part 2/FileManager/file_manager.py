# file_manager.py
import os
import shutil
import stat
import zipfile

class FileManager:
    def __init__(self, working_directory):
        self.working_directory = os.path.abspath(working_directory)
        self.current_directory = self.working_directory

    def _get_absolute_path(self, path):
        abs_path = os.path.abspath(os.path.join(self.current_directory, path))
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
        os.rmdir(path)  # Удаляет только пустые директории
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
        os.chmod(path, stat.S_IWRITE)  # Снимаем защиту "только для чтения"
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
        if not destination_path.startswith(self.working_directory):
            raise Exception("Access denied: нельзя переименовать файл за пределами рабочей директории.")
        os.rename(source_path, destination_path)
        return destination_path

    def get_current_directory(self):
        return self.current_directory

    # Дополнительные функции

    def archive_file(self, source, archive_name):
        """
        Архивирует указанный файл или директорию в zip-архив.
        source - имя файла или директории (относительно current_directory)
        archive_name - имя создаваемого архива (например, archive.zip)
        """
        source_path = self._get_absolute_path(source)
        archive_path = self._get_absolute_path(archive_name)
        with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zf:
            if os.path.isdir(source_path):
                for root, dirs, files in os.walk(source_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zf.write(file_path, os.path.relpath(file_path, os.path.dirname(source_path)))
            else:
                zf.write(source_path, os.path.basename(source_path))
        return archive_path

    def unarchive_file(self, archive_name, destination):
        """
        Разархивирует zip-архив в указанную директорию.
        archive_name - имя zip-архива (относительно current_directory)
        destination - директория для извлечения архива
        """
        archive_path = self._get_absolute_path(archive_name)
        dest_path = self._get_absolute_path(destination)
        with zipfile.ZipFile(archive_path, 'r') as zf:
            zf.extractall(dest_path)
        return dest_path

    def get_disk_quota(self):
        """
        Возвращает общее, использованное и свободное пространство в байтах
        для раздела, на котором находится рабочая директория.
        """
        total, used, free = shutil.disk_usage(self.working_directory)
        return total, used, free
