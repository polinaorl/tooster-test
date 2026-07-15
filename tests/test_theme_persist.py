import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage
from selenium.webdriver.common.by import By
import time

VALID_USER = "orlova.polina"
VALID_PASS = "+kWcR80WE9g="

def test_theme_persists_after_refresh(driver):
    print(" Авторизуюсь...")
    login_page = LoginPage(driver)
    login_page.login(VALID_USER, VALID_PASS)
    
    assert "login" not in driver.current_url.lower(), "Не удалось войти!"
    print(" Успешно вошел в систему")
    
    # Шаг 1: Переключаемся на тёмную тему
    print(" Переключаю на тёмную тему...")
    main_page = MainPage(driver)
    main_page.click_theme_settings()
    main_page.select_theme("dark")
    print(" Тема переключена")
    
    # Делаем скриншот ДО обновления
    driver.save_screenshot("before_refresh.png")
    print(" Скриншот 'before_refresh.png' (до обновления)")
    
    # Шаг 2: Обновляем страницу 
    print(" Обновляю страницу...")
    driver.refresh()
    
    # Ждём загрузки
    import time
    time.sleep(3)
    print("Страница обновлена")
    
    # Делаем скриншот ПОСЛЕ обновления
    driver.save_screenshot("after_refresh.png")
    print("Скриншот 'after_refresh.png' (после обновления)")
    
    # Шаг 3: Проверяем, что тема осталась тёмной
    body_bg = driver.execute_script("return window.getComputedStyle(document.body).backgroundColor")
    print(f" Цвет фона после обновления: {body_bg}")
    
    # Если тема тёмная, фон НЕ должен быть белым 
    if "255, 255, 255" in body_bg:
        print(" Фон белый — тема НЕ сохранилась!")
        assert False, "Тема не сохранилась после обновления (фон белый)"
    else:
        print(" Фон не белый — тема сохранилась!")
    
    # Шаг 4: Выход из системы 
    print(" Выхожу из системы...")
    try:
        # Ищем кнопку выхода 
        logout_button = driver.find_element(By.XPATH, "//*[contains(text(), 'выйти') or contains(text(), 'logout') or contains(text(), 'Выход')]")
        logout_button.click()
        print(" Вышел из системы")
    except:
        print(" Кнопка выхода не найдена (пропускаю)")
    
    print("Тест сохранения темы завершен!")