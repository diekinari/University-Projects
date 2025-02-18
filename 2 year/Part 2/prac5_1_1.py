import os
directory = input("Введите путь для создания директории: ")
if os.path.exists(directory):
    print("Директория уже существует")
else:
    os.makedirs(directory)
    print(f"Директория {directory} создана")

