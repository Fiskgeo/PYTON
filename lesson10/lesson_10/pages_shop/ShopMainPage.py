from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    def __init__(self, browser):
        self.driver =  browser
        self.driver.get("https://www.saucedemo.com/inventory.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()
        self.driver_find_element()


    def add_items_to_cart(self):
        """
                        Добавляем товары в корзину
        """
        self.driver_find_element( By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver_find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver_find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()


    def wait_for_cart_item(self):
        """
                                Ожидание появления товара в корзине
        """
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            ".shopping_cart_link[data-test='shopping_cart_link']"))).click()