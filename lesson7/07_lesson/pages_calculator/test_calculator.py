from pages_calculator import MainPage


def open_calculator(self):
    url = "https://bonigarcia.dev/selenium-webdriver-java/" \
          "slow-calculator.html"
    self.driver.get(url)











class MainPage:

    def set_cookie_policy(self):
        print("меня вызвали")

class Calculator:
    def __init__(self, driver):
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        calc = Calculator(driver)
        calc.open_calculator()
        driver.quit()





    def input_field(self):
        number = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        number.clear()
        number.send_keys("45")


    def input_symbols(self):
        button = self.driver.find_element(By.CSS_SELECTOR,
                                          "span.btn.btn-outline-primary")
        button.click()


        button_plus = self.driver.find_element(By.CSS_SELECTOR,
                                               "span.operator.btn \
                                                   .btn-outline-success")
        button_plus.click()


        button_eight = self.driver.find_element(By.XPATH, "//span[text()='8']")
        button_eight.click()


        button_equal = self.driver.find_element(By.CSS_SELECTOR,
                                                "span.btn.btn-outline-warning")
        button_equal.click()


        wait = WebDriverWait(driver, 45)
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,
                                                    "div.screen"), "15"))


    def check(self):
        assert self.driver.find_element(By.CSS_SELECTOR, "div.screen").text == "15"


    def calc(self):
        self.open_calculator()
        self.input_field()
        self.input_symbols()
        self.check()