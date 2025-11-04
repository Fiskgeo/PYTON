from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = None


class CartAddingPage:

        def cart_adding(self, driver):
            Sauce_Labs_Backpack_cart = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
            driver.implicitly_wait(4)

            Sauce_Labs_Bolt_T_Shirt_cart = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
            driver.implicitly_wait(4)

            Sauce_Labs_Onesie_cart = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
            driver.implicitly_wait(4)

class CartPage:
        def get_cart_content(self):
            return self._driver.find_element(By.CSS_SELECTOR, "#cart-content").text