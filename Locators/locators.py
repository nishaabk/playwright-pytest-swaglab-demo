class LoginLocators:
    USERNAME = "Username"
    PASSWORD = "Password"
    LOGIN_BUTTON = "button"
    ERROR_MESSAGE = ".error-message-container.error"

class LogoutLocators:
    OPEN_MENU = "#react-burger-menu-btn"
    LOGOUT = "#logout_sidebar_link"


class CartLocators:
    INVENTORY_ITEM = ".inventory_item"
    ADD_TO_CART = "Add to Cart"
    CART_LINK = ".shopping_cart_link"
    CART_ITEM = ".cart_item"
    REMOVE_BUTTON = "Remove"
    SORT_DROPDOWN = ".product_sort_container"
    CART_BADGE = ".shopping_cart_badge"


class CheckoutLocators:
    CHECKOUT_BUTTON = '[data-test="checkout"]'
    FIRST_NAME = "First Name"
    LAST_NAME = "Last Name"
    ZIP_CODE = "Zip/Postal Code"
    CONTINUE_BUTTON = '[data-test="continue"]'
    ERROR_MESSAGE = '[data-test="error"]'
    CANCEL_BUTTON = '[data-test="cancel"]'

class FinishLocators:
    SUCCESS_MESSAGE = ".complete-header"
    FINISH_BUTTON = '[data-test="finish"]'