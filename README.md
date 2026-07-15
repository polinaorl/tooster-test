# Автоматизированные тесты для Tooster

Репозиторий содержит UI-автотесты на Python с использованием pytest и Selenium WebDriver.

## Что тестируется
1. **Авторизация** (`test_auth.py`) – успешный вход в систему.
2. **Смена темы** (`test_theme.py`) – переключение на темную тему.
3. **Сохранение темы** (`test_theme_persist.py`) – тема сохраняется после перезагрузки.
4. **Создание каталога** (`test_catalog.py`) – создание каталога в папке "4 Орлова".
5. **Создание кейса** (`test_case.py`) – создание кейса в папке "4 Орлова".

## Требования
- Python 3.8+
- Google Chrome
- ChromeDriver

## Установка и запуск
Запустить все тесты сразу - pytest tests/ -v

Авторизация положительная - pytest tests/test_auth.py::test_positive_auth -v -s
Авторизация негативная - pytest tests/test_auth.py -v -s
Смена темы - pytest tests/test_theme.py -v -s
Сохранение темы - pytest tests/test_theme_persist.py -v -s
Создание кейса - pytest tests/test_case.py::test_create_case -v -s
Создание каталога - pytest tests/test_catalog.py::test_create_catalog -v -s
