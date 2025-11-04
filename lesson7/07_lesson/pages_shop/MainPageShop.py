from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = None


class MainPage:

        def __init__(self, driver):
            self._driver = driver
            self._driver.get("https://www.saucedemo.com/")
            self._driver.implicitly_wait(4)
            self._driver.maximize_window()
            self._driver.implicitly_wait(4)


