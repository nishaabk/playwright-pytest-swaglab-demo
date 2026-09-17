from Locators.locators import LogoutLocators
class LogoutPage:
        def __init__(self,page):
            self.page = page
        def logoutpage(self):
            self.page.locator(LogoutLocators.OPEN_MENU).click()
            self.page.locator(LogoutLocators.LOGOUT).click()