from Locators.locators import FinishLocators, CheckoutLocators

class Finishpage():
    def __init__(self, page):
        self.page = page

    def get_success_message(self):
        return self.page.locator(FinishLocators.SUCCESS_MESSAGE)

    def click_finish(self):
        self.page.locator(FinishLocators.FINISH_BUTTON).click()

    def click_cancel(self):
            self.page.locator(CheckoutLocators.CANCEL_BUTTON).click()


