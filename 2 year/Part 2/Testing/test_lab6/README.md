## Описание проекта
Автоматизированные тесты для проверки функциональности поиска на сайте Яндекс с
использованием Selenium WebDriver и паттерна Page Object Model.

## Технологический стек
- Python 3.8+
- Selenium WebDriver
- pytest
- Allure Framework
- Page Object Pattern

## Установка зависимостей
```bash
pip install -r requirements.txt
```
# Запуск тестов
## Обычный запуск
```bash
pytest tests/test_yandex_form.py -v
```

## С генерацией Allure отчетов
```bash
pytest --alluredir=allure-results
allure serve allure-results
```
