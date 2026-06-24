from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.test_data import BASE_URL, VALID_USERS, PASSWORD


def test_user_can_logout(page):
    login_page = LoginPage(page)

    login_page.navigate(BASE_URL)
    login_page.login(VALID_USERS[0], PASSWORD)

    page.click("#react-burger-menu-btn")
    page.click("#logout_sidebar_link")

    assert page.url == BASE_URL