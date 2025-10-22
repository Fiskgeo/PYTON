import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options = options)

def test_shopping():
    driver.get("https://www.saucedemo.com/")


    input_field = driver.find_element(By.ID, "user-name")
    input_field.send_keys("standard_user")

    input_field = driver.find_element(By.ID, "password")
    input_field.send_keys("secret_sauce")
    driver.implicitly_wait(4)

    login = driver.find_element(By.ID, "login-button").click()
    driver.implicitly_wait(4)

    Sauce_Labs_Backpack_cart = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.implicitly_wait(4)

    Sauce_Labs_Bolt_T_Shirt_cart = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.implicitly_wait(4)

    Sauce_Labs_Onesie_cart = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    driver.implicitly_wait(4)

    cart = driver.find_element(By.ID, "shopping_cart_container").click()
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
    driver.implicitly_wait(4)

    driver.quit()

    assert total == "Total: $58.29"




