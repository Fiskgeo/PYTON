from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = None


class LoginPage:

        def login_page(self, driver):
            input_field = driver.find_element(By.ID, "user-name")
            input_field.send_keys("standard_user")

            input_field = driver.find_element(By.ID, "password")
            input_field.send_keys("secret_sauce")
            driver.implicitly_wait(4)

            login = driver.find_element(By.ID, "login-button").click()
            driver.implicitly_wait(4)