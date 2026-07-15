import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

VALID_USER = "orlova.polina"
VALID_PASS = "+kWcR80WE9g="  

def test_positive_auth(driver):
    page = LoginPage(driver)
    page.login(VALID_USER, VALID_PASS)
    
    assert "login" not in driver.current_url.lower()
    print(" Позитивная авторизация прошла успешно!")

def test_negative_auth(driver):
    page = LoginPage(driver)
    page.login("wrong_user", "wrong_password")
    
    
    assert "login" in driver.current_url.lower()
    print(" Негативная авторизация: остались на странице входа")