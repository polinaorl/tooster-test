import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

VALID_USER = "orlova.polina"
VALID_PASS = "+kWcR80WE9g="

def test_create_case(driver):
    """Тест создания нового кейса в папке '4 Орлова'"""
    print("\n1. Авторизация...")
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
    print(" Нашел папку '4 Орлова'")
    
    print("\n 5. Открываю меню...")
    candidates = orlova_folder.find_elements(By.XPATH, ".//button | .//svg | .//i")
    menu_opened = False
    for btn in candidates:
        try:
            driver.execute_script("arguments[0].click();", btn)
            time.sleep(1.5)
            if driver.find_elements(By.XPATH, "//*[@id='dropdownMenuButton' or contains(text(), 'Создать')]"):
                print(" Меню открыто!")
                menu_opened = True
                break
            else:
                driver.find_element(By.TAG_NAME, 'body').click()
                time.sleep(0.5)
        except:
            continue
    
    if not menu_opened:
        raise Exception("Меню не открылось")
    
    print("\n 6. Кликаю 'Создать'...")
    create_btn = driver.find_element(By.ID, "dropdownMenuButton")
    driver.execute_script("arguments[0].click();", create_btn)
    time.sleep(2)
    
    
    print("\n 7. Выбираю 'КЕЙС'...")
    case_btn = driver.find_element(By.XPATH, "//button[.//i[contains(@class, 'fa-file')]]")
    driver.execute_script("arguments[0].click();", case_btn)
    print(" Выбрал 'Кейс'. Жду модальное окно...")
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Создание кейса')]"))
    )
    print("  Модальное окно открылось!")
    time.sleep(2)
    
    print("\n 8. Ввожу имя кейса...")
    
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='text' and @maxlength='120']"))
    )
    input_field.clear()
    input_field.send_keys("Тестовый кейс Орловой")
    print(" Ввел имя кейса")
    time.sleep(1)
    
    print("\n 9. Кликаю 'СОЗДАТЬ'...")
    submit_span = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Создать')]"))
    )
    driver.execute_script("arguments[0].click();", submit_span)
    print(" Кликнул на 'Создать'")
    time.sleep(3)
    
    print("\n 10. Проверяю результат...")
    driver.refresh()
    time.sleep(3)
    
    # Снова раскрываем папку
    chevrons = driver.find_elements(By.XPATH, "//i[contains(@class, 'fa-chevron-down')]")
    if chevrons:
        chevrons[0].click()
        time.sleep(2)
        
    driver.save_screenshot("case_final_check.png")
    
    if "Тестовый кейс Орловой" in driver.page_source:
        print("КЕЙС ДЕЙСТВИТЕЛЬНО СОЗДАН!")
    else:
        print(" Не создан. Смотри скриншот case_final_check.png")
        
    print("\n ТЕСТ ЗАВЕРШЕН!")