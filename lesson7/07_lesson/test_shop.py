import time
from selenium import webdriver
from pages_shop.MainPageShop import MainPage
from pages_shop.LoginPage import LoginPage
from pages_shop.CartPage import CartAddingPage
from pages_shop.CartPage import CartPage

def test_shop_buying():
    browser = webdriver.Chrome()
    main_page = MainPage(browser)
    login_page = LoginPage()
    login_page.login_page(browser)
    cart_adding = CartAddingPage()
    cart_adding.cart_adding(browser)
    time.sleep(8)



#cart_content = CartPage.get_cart_content(self)
#assert cart_content == "Ожидаемое содержимое"
