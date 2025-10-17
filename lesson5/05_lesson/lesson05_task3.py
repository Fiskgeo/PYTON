from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options = options)
driver.get("https://the-internet.herokuapp.com/inputs")
sleep(2)

input_field = driver.find_element(By.CSS_SELECTOR, "input")
input_field.send_keys("Sky")
sleep(2)

input_field.clear()

input_field.send_keys("Pro")
sleep(2)

driver.quit()
