import requests
from bs4 import BeautifulSoup
import pandas as pd
from fuzzywuzzy import fuzz
from serpapi import GoogleSearch
import time
import re
# Ваш API-ключ для SerpApi
SERP_API_KEY = "eff14df08b0954f788dd591fa47760fb7678095c80ee3de488abcb15d0eca021"

# Конфигурация
target_brand = "Дуб белфорд"
target_url_count = 1000  # Пробуем увеличить число сайтов для проверки


# Функция для поиска страниц через SerpApi
def search_pages(query, num_results=100):
    params = {
        "engine": "google",
        "q": query,
        "hl": None,
        "api_key": SERP_API_KEY,
        "num": num_results,
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    print(results)
    return [result['link'] for result in results.get("organic_results", [])]


# Функция для парсинга страницы и проверки совпадения
def parse_and_check_page(url, target_text):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Получаем текст страницы
        page_text = soup.get_text()

        # Нечеткое совпадение по целевому тексту
        match_score = fuzz.partial_ratio(target_text.lower(), page_text.lower())

        # Пытаемся найти цену (можно адаптировать по нужным сайтам)
        price = None
        price_candidates = soup.find_all(
            string=re.compile(r'\d+[\s,]*\d*\s?₽|руб\s?\d+[\s,]*\d*'))  # Пример: ищем цены в рублях
        if price_candidates:
            price = price_candidates[0].strip()

        return match_score >= 80, price  # Возвращаем совпадение и цену
    except requests.RequestException:
        return False, None  # Если запрос не удался, считаем, что совпадения нет


# Основная функция для парсинга и проверки
def main():
    search_query = f"{target_brand} лдсп кроностар kronostar плиты"
    urls = search_pages(search_query, num_results=target_url_count)
    print(len(urls))
    # Создаем пустой DataFrame для отчета
    data = []

    for url in urls:
        print(url)
        is_match, price = parse_and_check_page(url, target_brand)
        data.append({
            "URL": url,
            "Match Found": "Yes" if is_match else "No",
            "Price": price if price else "Не указана"  # Указываем, если цена не найдена
        })
        time.sleep(2)  # Пауза для избегания блокировки

    # Создаем DataFrame и выводим его в консоль
    df = pd.DataFrame(data)
    print(df)


if __name__ == "__main__":
    main()
