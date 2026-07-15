import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.binary_location = "/usr/bin/chromium-browser"
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")
    options.add_argument("--disable-extensions") 
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    
    time.sleep(2) # Пауза перед закрытием
    driver.quit()