import pytest

from pageobjects.LogoutPage import LogoutPage
from pageobjects.login import login
from test_data import VALID_USERS, INVALID_USERNAME
from utils.config_reader import ConfigReader
config = ConfigReader.get_config()

@pytest.mark.parametrize("username",VALID_USERS)
def test_logout(page,username):
    loginpage = login(page)
    loginpage.navigate()
    loginpage.login(username,config["password"])
    logout = LogoutPage(page)
    logout.logoutpage()
    assert page.locator("#login-button").is_visible()




