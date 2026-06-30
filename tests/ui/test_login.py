import re
from playwright.sync_api import expect
from pages.login_page import LoginPage


def test_login_page_loads(page, login_page):
    login_page.navigate()
    expect(page).to_have_title("Swag Labs")


def test_successful_login(page, login_page):
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url(re.compile("inventory"))
