from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = None


class BuyingPage:

        def buying_page(self, driver):

            driver.get("https://www.saucedemo.com/cart.html")
            driver.implicitly_wait(4)

            checkout = driver.find_element(By.ID, "checkout").click()
            driver.implicitly_wait(4)

            input_field = driver.find_element(By.ID, "first-name")
            input_field.send_keys("Yury")

            input_field = driver.find_element(By.ID, "last-name")
            input_field.send_keys("Volkov")

            input_field = driver.find_element(By.ID, "postal-code")
            input_field.send_keys("113326")
            driver.implicitly_wait(4)
            continue_button = driver.find_element(By.ID, "continue").click()
            driver.implicitly_wait(4)

            total = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
            total_value = float(total.split("$")[1])
            print(total)
            driver.implicitly_wait(4)

            driver.quit()

            assert total == "Total: $58.29"