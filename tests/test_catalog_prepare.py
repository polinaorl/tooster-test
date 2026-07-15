import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

VALID_USER = "orlova.polina"
VALID_PASS = "+kWcR80WE9g="

def test_catalog_prepare(driver):
    print("\n 1. Авторизация...")
    login_page = LoginPage(driver)
    login_page.login(VALID_USER, VALID_PASS)
    assert "login" not in driver.current_url.lower()
    print(" Вошел")
    
    print("\n 2. Перехожу в Кейс -> Список...")
    driver.find_element(By.XPATH, "//*[contains(text(), 'Кейс')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Список')]").click()
    time.sleep(5)
    print(" Перешел")
    
    print("\n 3. Раскрываю 1 Практика...")
    chevrons = driver.find_elements(By.XPATH, "//i[contains(@class, 'fa-chevron-down')]")
    if chevrons:
        chevrons[0].click()
        time.sleep(5)
        print(" Раскрыл")
    
    print("\n 4. Ищу папку '4 Орлова'...")
    orlova_folder = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//li[contains(@class, 'node') and contains(., 'Орлова')]"))
    )
    print("Нашел папку '4 Орлова'")
    
    print("\n⚙️ 5. Открываю меню...")
    candidates = orlova_folder.find_elements(By.XPATH, ".//button | .//svg | .//i")
    
    for btn in candidates:
        try:
            driver.execute_script("arguments[0].click();", btn)
            time.sleep(1.5)
            if driver.find_elements(By.XPATH, "//*[@id='dropdownMenuButton' or contains(text(), 'Создать')]"):
                print(" Меню открыто!")
                break
            else:
                driver.find_element(By.TAG_NAME, 'body').click()
                time.sleep(0.5)
        except:
            continue
    
    print("\n 6. Кликаю 'Создать'...")
    create_btn = driver.find_element(By.ID, "dropdownMenuButton")
    driver.execute_script("arguments[0].click();", create_btn)
    time.sleep(2)
    
    print("\n 7. Выбираю 'Каталог'...")
    catalog_btn = driver.find_element(By.XPATH, "//button[.//i[contains(@class, 'fa-folder')]]")
    driver.execute_script("arguments[0].click();", catalog_btn)
    
    print("\n 8. Жду модальное окно...")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Создание каталога')]"))
    )
    time.sleep(3)
    
    driver.save_screenshot("modal_ready_for_inspect.png")
    print("  Скриншот сохранен: modal_ready_for_inspect.png")
    
    input("\n>>> Модальное окно открыто <<<\n")
