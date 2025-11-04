from selenium import webdriver
from pages_shop.MainPageShop import MainPage
from pages_shop.LoginPage import LoginPage
from pages_shop.CartPage import CartAddingPage
from pages_shop.CartPage import CartPage

def test_shop_buying():
    browser = webdriver.Chrome()
    main_page = MainPage(browser)
    login_on_shop = LoginPage()
    cart_adding_goods = CartAddingPage


cart_content = CartPage.get_cart_content()
assert cart_content == "Ожидаемое содержимое"
