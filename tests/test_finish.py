from pageobjects.Finishpage import Finishpage
from pageobjects.cartpage import CartPage
from pageobjects.checkoutpage import CheckoutPage
from pageobjects.login import login
from test_data import VALID_USERS, PRODUCTS, CHECKOUT_USERS
from utils.config_reader import ConfigReader
config = ConfigReader.get_config()
#finish button
def test_complete_order(page):

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
    finish=Finishpage(page)
    finish.click_finish()
    assert (
        finish.get_success_message().text_content()
        == "Thank you for your order!"
    )
#cancel button
def test_cancel_order(page):

    loginpage = login(page)
    loginpage.navigate()
    loginpage.login(VALID_USERS[0],config["password"])
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
    # On Overview Page
    finish = Finishpage(page)
    finish.click_cancel()
    assert "inventory.html" in page.url