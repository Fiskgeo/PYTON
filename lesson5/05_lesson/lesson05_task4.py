from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options = options)
driver.get("http://the-internet.herokuapp.com/login")
sleep(2)

input_field = driver.find_element(By.CSS_SELECTOR, '[id = username]')
input_field.send_keys("tomsmith")
sleep(2)

input_field = driver.find_element(By.CSS_SELECTOR, '[id = password]')
input_field.send_keys("SuperSecretPassword!")
sleep(2)

input_field = driver.find_element(By.CSS_SELECTOR, "button.radius")
input_field.send_keys("Login")
input_field.click()
sleep(2)

driver.quit()