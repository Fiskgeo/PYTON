from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, browser):
        self.driver = browser
        self.driver.get("https://www.saucedemo.com/checkout-step-one.html")
        self.first_name_input = (By.ID, 'first_name')
        self.last_name_input = (By.ID, 'last_name')
        self.postal_code_input = (By.ID, 'postal_code')
        self.continue_button = (By.ID, 'continue')
        self.driver.get("https://www.saucedemo.com/checkout-step-two.html")
        self.total_price = (By.XPATH, "//div[@class='summary_total_label']")

    def enter_first_name_input(self, first_name):
        """
                Ввод имени.

                :param first_name: имя.
                :type first_name: str
                :return: None
        """
        first_name_input = self.driver.find_element(self.first_name_input)
        first_name_input.clear()
        first_name_input.send_keys('Алевтина')

    def enter_last_name_input(self, last_name):
        """
                        Ввод фамилии.
                        :param last_name: фамилия.
                        :type last_name: str
                        :return: None
        """
        last_name_input = self.driver.find_element(self.last_name_input)
        last_name_input.clear()
        last_name_input.send_keys('Смирнова')


    def enter_postal_code(self, postal_code):
        """
                                Ввод почтового кода.
                                :postal_code: почтовый код
                                :type postal_code: str
                                :return: None
        """
        postal_code_input = self.driver.find_element(self.postal_code_input)
        postal_code_input.clear()
        postal_code_input.send_keys('198324')

    def click_continue(self):
        """
                Нажимает кнопку продолжения.

                :return: True, если кнопка нажата успешно.
                :rtype: bool
        """
        continue_button = self.driver.find_element(self.continue_button)
        continue_button.click()
        WebDriverWait(self, driver, 10).untill(EC.presence_of_element_located((By.XPATH, "//div[@class='summary_total_label']")))

    def total_price(self):
        total_price_element = self.driver.find_element(self.total_price)
        return total_price_element.text