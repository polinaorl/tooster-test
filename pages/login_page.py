import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://185.61.26.174/"
        
        # Локаторы
        self.login_input = (By.CSS_SELECTOR, 'input[placeholder="Имя пользователя"]')
        self.password_input = (By.CSS_SELECTOR, 'input[type="password"]')
        self.login_button = (By.XPATH, "//button[contains(text(), 'Войти')]")

    def open(self):
        print(f"\n Открываю URL: {self.base_url}")
        self.driver.get(self.base_url)
        print(" Жду 3 секунды для загрузки...")
        time.sleep(3)

    def login(self, user, password):
        self.open()
        try:
            print(" Ищу поле логина...")
            login_field = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(self.login_input)
            )
            print(" Поле логина найдено! Ввожу данные...")
            login_field.clear()
            login_field.send_keys(user)
            
            print(" Ищу поле пароля...")
            pass_field = self.driver.find_element(*self.password_input)
            pass_field.clear()
            pass_field.send_keys(password)
            
            print(" Ищу кнопку 'Войти'...")
            self.driver.find_element(*self.login_button).click()
            print(" Нажал кнопку. Жду 2 секунды...")
            time.sleep(2)
            
        except Exception as e:
            print(f"\n ОШИБКА: Не удалось найти элемент!")
            print(f"Текст ошибки: {e}")
            
            # скриншот
            screenshot_name = "debug_screenshot.png"
            self.driver.save_screenshot(screenshot_name)
            print(f" Скриншот сохранен как '{screenshot_name}' в папке проекта!")
            print("Открой этот файл и посмотри, что там на самом деле.")
            raise