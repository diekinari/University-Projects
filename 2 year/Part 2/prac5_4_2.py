import os

print(f"Текущий рабочий каталог: {os.getcwd()}")
os.chdir(r'/usr')
print(f"Новый рабочий каталог: {os.getcwd()}")
print("Переменные окружения:")
for key, value in os.environ.items():
    print(f"{key}: {value}")