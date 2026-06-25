import pytest

from pages.login_page import LoginPage
from utils.test_data import (
    BASE_URL,
    VALID_USERS,
    PASSWORD,
    LOCKED_USER,
    INVALID_USER,
    INVALID_PASSWORD,
    INVALID_LOGIN_ERROR,
    LOCKED_OUT_ERROR,
    EMPTY_USERNAME_ERROR,
    EMPTY_PASSWORD_ERROR,
    INVENTORY_URL
)

@pytest.mark.parametrize("username", VALID_USERS)
def test_valid_login(page, username):
    login_page = LoginPage(page)
    
    login_page.navigate(BASE_URL)
    login_page.login(username, PASSWORD)
    assert login_page.is_inventory_page_loaded()
    assert "inventory.html" in page.url

def test_invalid_login_error_message(page):
    login_page = LoginPage(page)

    login_page.navigate(BASE_URL)
    login_page.login(INVALID_USER, INVALID_PASSWORD)

    assert login_page.is_error_message_visible()
    assert INVALID_LOGIN_ERROR == login_page.get_error_message()

def test_locked_out_user_shows_error_message(page):
    login_page = LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login(LOCKED_USER, PASSWORD)
    assert login_page.is_error_message_visible()
    assert login_page.get_error_message() == LOCKED_OUT_ERROR

def test_login_with_empty_username_shows_error(page):
    login_page = LoginPage(page)

    login_page.navigate(BASE_URL)
    login_page.login("", PASSWORD)

    assert login_page.is_error_message_visible()
    assert login_page.get_error_message() == EMPTY_USERNAME_ERROR


def test_login_with_empty_password_shows_error(page):
    login_page = LoginPage(page)

    login_page.navigate(BASE_URL)
    login_page.login(VALID_USERS[0], "")

    assert login_page.is_error_message_visible()
    assert login_page.get_error_message() == EMPTY_PASSWORD_ERROR


def test_login_with_empty_username_and_password_shows_error(page):
    login_page = LoginPage(page)

    login_page.navigate(BASE_URL)
    login_page.login("", "")

    assert login_page.is_error_message_visible()
    assert login_page.get_error_message() == EMPTY_USERNAME_ERROR


def test_direct_inventory_access_without_login_redirects_to_login(page):
    page.goto(INVENTORY_URL)

    assert page.url == BASE_URL
    assert page.locator("#login-button").is_visible()