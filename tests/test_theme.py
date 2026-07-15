import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage

VALID_USER = "orlova.polina"
VALID_PASS = "+kWcR80WE9g="

def test_change_theme(driver):
    print(" Авторизуюсь...")
    login_page = LoginPage(driver)
    login_page.login(VALID_USER, VALID_PASS)
    
    assert "login" not in driver.current_url.lower(), "Не удалось войти!"
    print(" Успешно вошел в систему")
    
    main_page = MainPage(driver)
    main_page.click_theme_settings()
    main_page.select_theme("dark")
    
    driver.save_screenshot("theme_result.png")
    print(" Скриншот результата сохранен как 'theme_result.png'")
    print(" Тест смены темы завершен!")