import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from MainPageCalculator import CalculatorPage
import allure

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
    yield driver
    driver.quit()

@allure.title("Тест калькулятора")
@allure.description("Вызов онлайн калькулятора и выполнение действий")
@allure.feature("READ")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculate_delay(driver):

    calculator_page = CalculatorPage(driver)
    with allure.step("установка задержки 45 секунд"):
        calculator_page.set_delay(45)
    with allure.step("ввод числа 7"):
        calculator_page.click_button("7")
    with allure.step("ввод знака сложение"):
        calculator_page.click_button("+")
    with allure.step("ввод числа 8"):
        calculator_page.click_button("8")
    with allure.step("ввод знака равно"):
        calculator_page.click_button("=")
    with allure.step("Ожидание результата"):
        calculator_page.wait_result("15")
    with allure.step("Сравнить что полученный результат равен 15"):
        assert driver.find_element(By.CSS_SELECTOR, ".screen").text == "15"