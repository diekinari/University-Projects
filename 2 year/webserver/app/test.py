from requests import *


a = get(url="https://org.fa.ru")

print(a.content)
