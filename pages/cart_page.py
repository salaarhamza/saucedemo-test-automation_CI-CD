class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_item = ".cart_item"
        self.cart_item_name = ".inventory_item_name"
        self.cart_badge = ".shopping_cart_badge"
        self.checkout_button = "[data-test='checkout']"
        self.continue_shopping_button = "[data-test='continue-shopping']"

    def get_cart_item_count(self):
        return self.page.locator(self.cart_item).count()

    def get_cart_item_names(self):
        return self.page.locator(self.cart_item_name).all_inner_texts()

    def get_cart_badge_count(self):
        if self.page.locator(self.cart_badge).count() == 0:
            return None
        return self.page.locator(self.cart_badge).inner_text()

    def remove_backpack_from_cart(self):
        self.page.click("[data-test='remove-sauce-labs-backpack']")

    def remove_bike_light_from_cart(self):
        self.page.click("[data-test='remove-sauce-labs-bike-light']")

    def continue_shopping(self):
        self.page.click(self.continue_shopping_button)

    def proceed_to_checkout(self):
        self.page.click(self.checkout_button)