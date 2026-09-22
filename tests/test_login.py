
import pytest
from pageobjects.login import login
from test_data import VALID_USERS, INVALID_PASSWORD, BLANK_VALUE, INVALID_USERNAME
from utils.config_reader import ConfigReader
from utils.custom_logger import LogGen

config = ConfigReader.get_config()
logger=LogGen.loggen()

#we are using parametrize here because we are executing same test step with different data sets
@pytest.mark.parametrize("username",VALID_USERS)
#validusername and password
def test_loginpage(username,page):
    logger.info("Starting Login Test")
    loginpage=login(page)
    loginpage.navigate()

    logger.info(f"Attempting login using{username}")
    loginpage.login(username,config["password"])
    assert "inventory.html" in page.url
    logger.info("Login Successful")


#invalidusername
@pytest.mark.parametrize("username",INVALID_USERNAME)
def test_invalidusername(page,username):
    loginpage = login(page)
    loginpage.navigate()
    loginpage.login(username, config["password"])
    assert loginpage.errormessage().is_visible()

#invalidpassword
@pytest.mark.parametrize("username",VALID_USERS)
def test_invalidpassword(page,username):
    loginpage = login(page)
    loginpage.navigate()
    loginpage.login(username,INVALID_PASSWORD)
    assert loginpage.errormessage().is_visible()

@pytest.mark.parametrize("username",VALID_USERS)
#blankpassword
def test_blankpassword(page,username):
    loginpage = login(page)
    loginpage.navigate()
    loginpage.login(username,BLANK_VALUE)
    assert loginpage.errormessage().is_visible()

#blankusername
def test_blankusername(page):
    loginpage = login(page)
    loginpage.navigate()
    loginpage.login(BLANK_VALUE,config["password"])
    assert loginpage.errormessage().is_visible()





