import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    # Инициализация драйвера
    driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
    )

    # Неявное ожидание
    driver.implicitly_wait(10)

    yield driver

    driver.quit()

@pytest.fixture
def base_url():
    return "https://ya.ru"