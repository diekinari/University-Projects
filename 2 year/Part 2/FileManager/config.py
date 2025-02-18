# config.py
import configparser
import os

CONFIG_FILE = 'config.ini'

def load_config():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    working_directory = config.get('DEFAULT', 'working_directory', fallback=os.getcwd())
    # Приводим путь к абсолютному виду
    working_directory.replace(" ", "\ ")
    working_directory = os.path.abspath(working_directory)
    return working_directory

print(load_config())
