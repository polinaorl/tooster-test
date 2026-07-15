from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.binary_location = "/usr/bin/chromium-browser"
options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    print("1. Вхожу в систему...")
    driver.get("https://185.61.26.174/")
    time.sleep(3)
    
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Имя пользователя"]').send_keys("orlova.polina")
    driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys("+kWcR80WE9g=")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]").click()
    time.sleep(3)
    
    print("2. Перехожу в Кейс -> Список...")
    driver.find_element(By.XPATH, "//*[contains(text(), 'Кейс')]").click()
    time.sleep(1.5)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Список')]").click()
    time.sleep(5)
    
    print("3. Раскрываю '1 Практика'...")
    try:
        chevron = driver.find_element(By.XPATH, "//i[contains(@class, 'fa-chevron-down')]")
        chevron.click()
        time.sleep(3)
        print("Раскрыл")
    except:
        print("Не раскрыл")
    
    
    
    input("\n>>> Нажми <<<\n")

finally:
    driver.quit()
