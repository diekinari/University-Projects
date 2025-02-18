# user_manager.py
import os
import json
import getpass
import hashlib

USERS_FILE = 'users.json'
USERS_DIR = 'users'  # каталог, в котором будут создаваться персональные директории

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_users(users):
    with open(USERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(users, f, indent=4)

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def register_user(base_directory):
    users = load_users()
    username = input("Введите имя пользователя для регистрации: ").strip()
    if username in users:
        print("Пользователь с таким именем уже существует!")
        return None
    password = getpass.getpass("Введите пароль: ")
    password_confirm = getpass.getpass("Подтвердите пароль: ")
    if password != password_confirm:
        print("Пароли не совпадают!")
        return None
    users[username] = hash_password(password)
    save_users(users)
    # Создаем персональную директорию для пользователя
    user_dir = os.path.join(base_directory, USERS_DIR, username)
    os.makedirs(user_dir, exist_ok=True)
    print(f"Пользователь '{username}' успешно зарегистрирован.")
    return username

def login_user(base_directory):
    users = load_users()
    username = input("Введите имя пользователя: ").strip()
    if username not in users:
        print("Пользователь не найден.")
        return None
    password = getpass.getpass("Введите пароль: ")
    if users[username] != hash_password(password):
        print("Неверный пароль!")
        return None
    # Убедимся, что персональная директория существует
    user_dir = os.path.join(base_directory, USERS_DIR, username)
    os.makedirs(user_dir, exist_ok=True)
    print(f"Пользователь '{username}' успешно авторизован.")
    return username
