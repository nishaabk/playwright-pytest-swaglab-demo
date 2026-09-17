from Locators.locators import LoginLocators
from utils.config_reader import ConfigReader
from utils.custom_logger import LogGen

config = ConfigReader.get_config()
class login:
    logger=LogGen.loggen()

    def __init__(self,page):
        self.page=page

    def navigate(self):
        self.logger.info("Navigating to application URL")
        self.page.goto(config["url"])

    def login(self,username,password):
        self.logger.info(f"Entering username:{username}")
        self.page.get_by_placeholder(LoginLocators.USERNAME).fill(username)

        self.logger.info("Entering password")
        self.page.get_by_placeholder(LoginLocators.PASSWORD).fill(password)

        self.logger.info("Clicking login button")
        self.page.get_by_role(LoginLocators.LOGIN_BUTTON).click()

    def errormessage(self):
        return self.page.locator(LoginLocators.ERROR_MESSAGE)



