import time
import pytest

@pytest.fixture(scope="function")
def page(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    time.sleep(5)
    browser.close()
