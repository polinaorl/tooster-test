import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        
        self.theme_icon = (By.XPATH, "//*[contains(@class, 'settings') or contains(@class, 'theme') or contains(@title, 'тема')]")
        
    def click_theme_settings(self):
        print(" Ищу иконку настроек темы...")
        try:
            icon = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.theme_icon)
            )
            try:
                icon.click()
            except:
                self.driver.execute_script("arguments[0].click();", icon)
            print("Нажал на иконку настроек темы")
            time.sleep(1.5)
        except Exception as e:
            print(f" Не нашел иконку настроек: {e}")
            self.driver.save_screenshot("theme_debug.png")
            raise

    def select_theme(self, theme_name="dark"):
        """Выбираем тему по цвету кружочка (0-синий, 1-тёмно-синий, 2-красный, 3-чёрный)"""
        print(f" Выбираю тему: {theme_name} (клик на кружочек)...")
        
        # Ищем все кружочки с темами 
        try:
            # Ждем появления кружочков
            circles = WebDriverWait(self.driver, 10).until(
                EC.presence_of_elements_located((By.CSS_SELECTOR, '[class*="theme"] circle, [class*="color"] circle, circle'))
            )
            
            print(f" Найдено кружочков с темами: {len(circles)}")
            
            
            if len(circles) >= 2:
                # Пробуем кликнуть на предпоследний или последний
                target_circle = circles[-1]  # Последний (чёрный)
                self.driver.execute_script("arguments[0].click();", target_circle)
                print(" Кликнул на кружочек темы (последний)")
            else:
                # Если кружочков мало, кликаем на любой
                self.driver.execute_script("arguments[0].click();", circles[0])
                print(" Кликнул на первый кружочек темы")
                
            time.sleep(2)
            
        except Exception as e:
            print(f" Не нашел кружочки с темами: {e}")
            
            try:
                print(" Пробую альтернативный метод...")
                buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button, [role="button"]')
                if buttons:
                    buttons[-1].click()  
                    print("Кликнул на последнюю кнопку")
            except:
                self.driver.save_screenshot("theme_debug.png")
                raise