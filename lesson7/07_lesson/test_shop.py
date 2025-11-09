from selenium import webdriver
from pages_shop.MainPageShop import MainPage
from pages_shop.LoginPage import LoginPage
from pages_shop.CartPage import CartAddingPage
from pages_shop.CartPage import CartPage
from pages_shop.BuyingPage import BuyingPage

def test_shop_buying():
    browser = webdriver.Edge()
    main_page = MainPage(browser)
    login_page = LoginPage()
    login_page.login_page(browser)
    cart_adding = CartAddingPage()
    cart_adding.cart_adding(browser)
    buying_page = BuyingPage()
    buying_page.buying_page(browser)








