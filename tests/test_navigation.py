from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.navigation_page import NavigationPage
from utils.test_data import BASE_URL, VALID_USERS, PASSWORD


# add page-object helper to InventoryPage for checking add-to-cart backpack visibility
def _is_backpack_add_button_visible(self):
    return self.page.locator("[data-test='add-to-cart-sauce-labs-backpack']").is_visible()

InventoryPage.is_backpack_add_button_visible = _is_backpack_add_button_visible


def login_as_standard_user(page):
    login_page = LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login(VALID_USERS[0], PASSWORD)


def test_all_items_link_returns_to_inventory_page_from_cart(page):
    login_as_standard_user(page)

    inventory_page = InventoryPage(page)
    inventory_page.open_cart()

    navigation_page = NavigationPage(page)
    navigation_page.click_all_items()

    assert "inventory.html" in page.url


def test_about_link_has_expected_url(page):
    login_as_standard_user(page)

    navigation_page = NavigationPage(page)

    assert navigation_page.get_about_href() == "https://saucelabs.com/"


def test_logout_ends_session_and_returns_to_login_page(page):
    login_as_standard_user(page)

    navigation_page = NavigationPage(page)
    navigation_page.logout()

    assert page.url == BASE_URL
    assert page.locator("#login-button").is_visible()


def test_reset_app_state_empties_cart_and_resets_buttons(page):
    login_as_standard_user(page)

    inventory_page = InventoryPage(page)
    inventory_page.add_backpack_to_cart()

    assert inventory_page.get_cart_badge_count() == "1"
    assert inventory_page.is_backpack_remove_button_visible()

    navigation_page = NavigationPage(page)
    navigation_page.reset_app_state()

    assert navigation_page.get_cart_badge_count() == 0

def test_footer_social_links_have_expected_href_values(page):
    login_as_standard_user(page)

    navigation_page = NavigationPage(page)

    twitter_href = page.locator("[data-test='social-twitter']").get_attribute("href")
    facebook_href = page.locator("[data-test='social-facebook']").get_attribute("href")
    linkedin_href = page.locator("[data-test='social-linkedin']").get_attribute("href")

    assert twitter_href == "https://twitter.com/saucelabs"
    assert facebook_href == "https://www.facebook.com/saucelabs"
    assert linkedin_href == "https://www.linkedin.com/company/sauce-labs/"