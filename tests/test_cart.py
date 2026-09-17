from pageobjects.cartpage import CartPage
from pageobjects.login import login
from test_data import PRODUCTS, VALID_USERS
from test_data import SORT_OPTIONS
from test_data import PRODUCTS
from utils.config_reader import ConfigReader
config = ConfigReader.get_config()

#add products
def test_add_product(page):
    loginpage = login(page)
    loginpage.navigate()
    loginpage.login(VALID_USERS[0],config["password"])
    cart = CartPage(page)
    product = PRODUCTS[0]
    cart.add_product(product)
    cart.open_cart()
    assert cart.is_product_present(product)

#multiple products
def test_add_multiple_products(page):
    loginpage = login(page)
    loginpage.navigate()
    loginpage.login(VALID_USERS[0],config["password"])
    cart = CartPage(page)
    cart.add_multiple_products(PRODUCTS)
    cart.open_cart()
    for product in PRODUCTS:
     assert cart.is_product_present(product)

#removeproducts
def test_remove_product(page):
    loginpage = login(page)
    loginpage.navigate()
    loginpage.login(VALID_USERS[0], config["password"])
    cart = CartPage(page)
    product = PRODUCTS[0]
    cart.add_product(product)
    cart.open_cart()
    cart.remove_product(product)
    assert not cart.is_product_present(product)


#sort products
def test_sort_products(page):
    loginpage = login(page)
    loginpage.navigate()
    loginpage.login(VALID_USERS[0], config["password"])
    cart = CartPage(page)
    cart.sort_products(SORT_OPTIONS[1])

