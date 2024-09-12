from requests import Session
from bs4 import BeautifulSoup as bs
import urllib3
import certifi

login = '237455'
password = 'AAei7567'

http = urllib3.PoolManager(
    cert_reqs="CERT_REQUIRED",
    ca_certs=certifi.where()
)

resp = http.request("GET", "https://org.fa.ru")
print(resp.data)

# with Session() as s:
#     site = s.get("https://org.fa.ru/app/profile/marks", verify=False)
#     bs_content = bs(site.content, 'html.parser')
#     login_data = {"USER_LOGIN": login, "USER_PASSWORD": password}
#     s.post("https://org.fa.ru/app/profile/marks")
#     home_page = s.get("https://org.fa.ru/app/profile/marks")
#     print(home_page.content)