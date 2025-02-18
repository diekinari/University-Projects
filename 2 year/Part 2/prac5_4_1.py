import os, platform, psutil
print(f"ОС: {platform.system()} {platform.release()}")
print(f"Версия Python: {platform.python_version()}")
print(f"Свободно на диске: {psutil.disk_usage('/').free / (1024**3):.2f} GB")