from Locators.locators import CheckoutLocators

class CheckoutPage:

    def __init__(self, page):
        self.page = page

    def click_checkout(self):
        self.page.locator(CheckoutLocators.CHECKOUT_BUTTON).click()

    def enter_checkout_details(self,first_name,last_name,zip_code):
        self.page.get_by_placeholder( CheckoutLocators.FIRST_NAME).fill(first_name)
        self.page.get_by_placeholder(CheckoutLocators.LAST_NAME).fill(last_name)
        self.page.get_by_placeholder( CheckoutLocators.ZIP_CODE).fill(zip_code)

    def click_continue(self):
        self.page.locator(CheckoutLocators.CONTINUE_BUTTON).click()

    def get_error_message(self):
        return self.page.locator(CheckoutLocators.ERROR_MESSAGE )

    def click_cancel(self):
            self.page.locator(CheckoutLocators.CANCEL_BUTTON).click()