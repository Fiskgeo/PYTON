import pytest
from selenium import webdriver
from ShopPage import *
import allure
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()
@allure.title("Тест онлайн-магазина")
@allure.description("Переход на страницу магазина, авторизация, выбор товаров, расчёт итоговой цены")
@allure.feature("READ")
@allure.severity(allure.severity_level.CRITICAL)
def test_purchases(driver):

    """
                           Авторизация
    """
    with allure.step("страница магазина"):
        login_page = LoginPage(driver)
    with allure.step("ввод логина"):
        login_page.enter_username('standard_user')
    with allure.step("ввод пароля"):
        login_page.enter_password('secret_sauce')
    with allure.step("вход"):
        login_page.enter_login()


    """
                               Добавление товаров в корзину
    """
    main_page = MainPage(driver)
    with allure.step("добавление товара в корзину"):
        main_page.add_items_to_cart()


    """
                                   Переход в корзину
    """
    with allure.step("переход в корзину"):
        main_page.wait_for_cart_item()


    """
                                       Нажатие на кнопку
    """
    cart_page = CartPage(driver)
    with allure.step("нажатие на кнопку"):
        cart_page.click_continue()


    """
                                          Заполнение формы данными
    """
    checkout_page = CheckoutPage(driver)
    with allure.step("ввод имени"):
        checkout_page.enter_first_name_input()
    with allure.step("ввод фамилии"):
        checkout_page.enter_last_name_input()
    with allure.step("ввод почтового кода"):
        checkout_page.enter_postal_code()
    with allure.step("нажатие кнопки"):
        checkout_page.click_continue()


    """
                                              Проверить, что итоговая сумма равна $58.29
    """
    with allure.step("проверка итоговой суммы"):
        assert checkout_page.total_price() == "Total: $58.29"