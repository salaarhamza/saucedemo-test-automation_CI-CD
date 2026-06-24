from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.test_data import BASE_URL, VALID_USERS, PASSWORD

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.test_data import BASE_URL, VALID_USERS, PASSWORD


def login_as_standard_user(page):
    login_page = LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login(VALID_USERS[0], PASSWORD)


def test_all_products_render_with_required_information(page):
    login_as_standard_user(page)
    inventory_page = InventoryPage(page)

    names = inventory_page.get_product_names()
    descriptions = inventory_page.get_product_descriptions()
    prices = inventory_page.get_product_prices()

    assert inventory_page.get_product_count() == 6
    assert len(names) == 6
    assert len(descriptions) == 6
    assert len(prices) == 6
    assert inventory_page.get_product_image_count() == 6

    assert all(name.strip() for name in names)
    assert all(description.strip() for description in descriptions)
    assert all(price > 0 for price in prices)


def test_sort_products_by_name_a_to_z(page):
    login_as_standard_user(page)
    inventory_page = InventoryPage(page)

    inventory_page.sort_by_name_a_to_z()
    product_names = inventory_page.get_product_names()

    assert product_names == sorted(product_names)


def test_sort_products_by_name_z_to_a(page):
    login_as_standard_user(page)
    inventory_page = InventoryPage(page)

    inventory_page.sort_by_name_z_to_a()
    product_names = inventory_page.get_product_names()

    assert product_names == sorted(product_names, reverse=True)


def test_sort_products_by_price_low_to_high(page):
    login_as_standard_user(page)
    inventory_page = InventoryPage(page)

    inventory_page.sort_by_price_low_to_high()
    product_prices = inventory_page.get_product_prices()

    assert product_prices == sorted(product_prices)


def test_sort_products_by_price_high_to_low(page):
    login_as_standard_user(page)
    inventory_page = InventoryPage(page)

    inventory_page.sort_by_price_high_to_low()
    product_prices = inventory_page.get_product_prices()

    assert product_prices == sorted(product_prices, reverse=True)


def test_add_one_product_to_cart_updates_badge_and_button(page):
    login_as_standard_user(page)
    inventory_page = InventoryPage(page)

    inventory_page.add_backpack_to_cart()

    assert inventory_page.get_cart_badge_count() == "1"
    assert inventory_page.is_backpack_remove_button_visible()


def test_add_multiple_products_to_cart_updates_badge_count(page):
    login_as_standard_user(page)
    inventory_page = InventoryPage(page)

    inventory_page.add_backpack_to_cart()
    inventory_page.add_bike_light_to_cart()

    assert inventory_page.get_cart_badge_count() == "2"


def test_remove_product_from_inventory_updates_badge_count(page):
    login_as_standard_user(page)
    inventory_page = InventoryPage(page)

    inventory_page.add_backpack_to_cart()
    inventory_page.add_bike_light_to_cart()
    inventory_page.remove_backpack_from_cart()

    assert inventory_page.get_cart_badge_count() == "1"


def test_add_all_products_to_cart_updates_badge_count(page):
    login_as_standard_user(page)
    inventory_page = InventoryPage(page)

    inventory_page.add_all_products_to_cart()

    assert inventory_page.get_cart_badge_count() == "6"


def test_clicking_product_name_opens_product_detail_page(page):
    login_as_standard_user(page)
    inventory_page = InventoryPage(page)

    inventory_page.open_backpack_detail_by_name()

    assert "inventory-item.html?id=4" in page.url
    assert page.locator(".inventory_details_name").inner_text() == "Sauce Labs Backpack"


def test_clicking_product_image_opens_product_detail_page(page):
    login_as_standard_user(page)
    inventory_page = InventoryPage(page)

    inventory_page.open_backpack_detail_by_image()

    assert "inventory-item.html?id=4" in page.url
    assert page.locator(".inventory_details_name").inner_text() == "Sauce Labs Backpack"


def test_cart_icon_navigates_to_cart_page(page):
    login_as_standard_user(page)
    inventory_page = InventoryPage(page)

    inventory_page.open_cart()

    assert "cart.html" in page.url