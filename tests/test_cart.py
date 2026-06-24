from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.test_data import BASE_URL, VALID_USERS, PASSWORD


def login_and_add_two_products_to_cart(page):
    login_page = LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login(VALID_USERS[0], PASSWORD)

    inventory_page = InventoryPage(page)
    inventory_page.add_backpack_to_cart()
    inventory_page.add_bike_light_to_cart()
    inventory_page.open_cart()


def test_cart_lists_exactly_added_items(page):
    login_and_add_two_products_to_cart(page)
    cart_page = CartPage(page)

    cart_items = cart_page.get_cart_item_names()

    assert cart_page.get_cart_item_count() == 2
    assert "Sauce Labs Backpack" in cart_items
    assert "Sauce Labs Bike Light" in cart_items


def test_removing_item_from_cart_updates_list_and_badge(page):
    login_and_add_two_products_to_cart(page)
    cart_page = CartPage(page)

    cart_page.remove_backpack_from_cart()

    cart_items = cart_page.get_cart_item_names()

    assert cart_page.get_cart_item_count() == 1
    assert "Sauce Labs Backpack" not in cart_items
    assert "Sauce Labs Bike Light" in cart_items
    assert cart_page.get_cart_badge_count() == "1"


def test_removing_all_items_leaves_cart_empty_and_badge_hidden(page):
    login_and_add_two_products_to_cart(page)
    cart_page = CartPage(page)

    cart_page.remove_backpack_from_cart()
    cart_page.remove_bike_light_from_cart()

    assert cart_page.get_cart_item_count() == 0
    assert cart_page.get_cart_badge_count() is None


def test_continue_shopping_returns_to_inventory_page(page):
    login_and_add_two_products_to_cart(page)
    cart_page = CartPage(page)

    cart_page.continue_shopping()

    assert "inventory.html" in page.url


def test_checkout_button_navigates_to_checkout_step_one(page):
    login_and_add_two_products_to_cart(page)
    cart_page = CartPage(page)

    cart_page.proceed_to_checkout()

    assert "checkout-step-one.html" in page.url