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
    page.screenshot(path="../Results/screenshot.png")

@pytest.mark.parametrize("username", INVALID_USERNAME)
def test_logoutfailure(page, username):
    page.context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    try:
        loginpage = login(page)
        loginpage.navigate()
        loginpage.login(username,config["password"])
        page.screenshot(path="../Results/screenshot2.png")
        logout = LogoutPage(page)
        logout.logoutpage()
        assert page.locator("#login-button").is_visible()
    finally:
        page.context.tracing.stop(path="../Results/trace.zip")


