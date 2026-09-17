import pytest
from pageobjects.login import login
from pageobjects.cartpage import CartPage
from pageobjects.checkoutpage import CheckoutPage
from utils.config_reader import ConfigReader
config = ConfigReader.get_config()


from test_data import (
    VALID_USERS,
    PRODUCTS,
    CHECKOUT_USERS, INVALID_CHECKOUT_DATA
)

def test_successful_checkout(page):

    loginpage = login(page)
    loginpage.navigate()
    loginpage.login(
        VALID_USERS[0],
        config["password"]
    )
    cart = CartPage(page)
    cart.add_product(PRODUCTS[0])
    cart.open_cart()
    checkout = CheckoutPage(page)
    checkout.click_checkout()
    user = CHECKOUT_USERS[0]
    checkout.enter_checkout_details(
        user["first_name"],
        user["last_name"],
        user["zip_code"]
    )

    checkout.click_continue()
    assert "checkout-step-two" in page.url

@pytest.mark.parametrize(
    "firstname,lastname,zipcode",
    INVALID_CHECKOUT_DATA)
def test_invalid_checkout(
        page,
        firstname,
        lastname,
        zipcode):
    loginpage = login(page)
    loginpage.navigate()
    loginpage.login(
        VALID_USERS[0],
        config["password"]
    )

    cart = CartPage(page)
    cart.add_product(PRODUCTS[0])
    cart.open_cart()
    checkout = CheckoutPage(page)
    checkout.click_checkout()
    checkout.enter_checkout_details(
        firstname,
        lastname,
        zipcode
    )

    checkout.click_continue()
    assert checkout.get_error_message().is_visible()


def test_checkout_cancel(page):
    loginpage = login(page)
    loginpage.navigate()
    loginpage.login(
        VALID_USERS[0],
        config["password"]
    )

    cart = CartPage(page)
    cart.add_product(PRODUCTS[0])
    cart.open_cart()
    checkout = CheckoutPage(page)
    checkout.click_checkout()
    checkout.click_cancel()
    assert "cart.html" in page.url