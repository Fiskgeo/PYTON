import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
def test_form():
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.implicitly_wait(4)

    element = driver.find_element(By.NAME, 'first-name')
    element.send_keys("Иван")
    driver.implicitly_wait(4)

    element = driver.find_element(By.NAME, 'last-name')
    element.send_keys("Петров")
    driver.implicitly_wait(4)

    element = driver.find_element(By.NAME, 'address')
    element.send_keys("Ленина, 55-3")
    driver.implicitly_wait(4)

    element = driver.find_element(By.NAME, 'e-mail')
    element.send_keys("test@skypro.com")
    driver.implicitly_wait(4)

    element = driver.find_element(By.NAME, 'phone')
    element.send_keys("+7985899998787")
    driver.implicitly_wait(4)

    element = driver.find_element(By.NAME, 'city')
    element.send_keys("Москва")
    driver.implicitly_wait(4)

    element = driver.find_element(By.NAME, 'country')
    element.send_keys("Россия")
    driver.implicitly_wait(4)

    element = driver.find_element(By.NAME, 'job-position')
    element.send_keys("QA")
    driver.implicitly_wait(4)


    element = driver.find_element(By.NAME, 'company')
    element.send_keys("SkyPro")
    driver.implicitly_wait(4)

    element = driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary")
    element.submit()
    driver.implicitly_wait(4)


    zip_code = driver.find_element(By.ID, 'zip-code').value_of_css_property("background-color")




    assert zip_code == "rgba(248, 215, 218, 1)"
    fields = ["first-name", "last-name", "address", "city", "country", "e-mail", "phone", "job-position", "company"]

    for field_id in fields:
        wait = WebDriverWait(driver, 2)
        field_element = wait.until(EC.visibility_of_element_located((By.ID, field_id)))
        border_color = field_element.value_of_css_property("border-color")
    assert border_color == "rgb(186, 219, 204)" in border_color, f"Поле {field_id} не подсвечено зеленым"
    waiter = WebDriverWait(driver, 20)
    driver.quit()

