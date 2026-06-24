class InventoryPage:

    def __init__(self, page):
        self.page = page
        self.inventory_container = ".inventory_list"
        self.inventory_items = ".inventory_item"
        self.product_names = ".inventory_item_name"
        self.product_descriptions = ".inventory_item_desc"
        self.product_prices = ".inventory_item_price"
        self.product_images = ".inventory_item_img img"
        self.sort_dropdown = "[data-test='product-sort-container']"
        self.cart_link = ".shopping_cart_link"
        self.cart_badge = ".shopping_cart_badge"

    def is_loaded(self):
        return self.page.locator(self.inventory_container).is_visible()

    def get_product_count(self):
        return self.page.locator(self.inventory_items).count()

    def get_product_names(self):
        return self.page.locator(self.product_names).all_inner_texts()
    def get_product_descriptions(self):
        return self.page.locator(self.product_descriptions).all_inner_texts()

    def get_product_prices(self):
        price_texts = self.page.locator(self.product_prices).all_inner_texts()
        return [float(price.replace("$", "")) for price in price_texts]

    def get_product_image_count(self):
        return self.page.locator(self.product_images).count()

    def sort_by_name_a_to_z(self):
        self.page.select_option(self.sort_dropdown, "az")

    def sort_by_name_z_to_a(self):
        self.page.select_option(self.sort_dropdown, "za")

    def sort_by_price_low_to_high(self):
        self.page.select_option(self.sort_dropdown, "lohi")

    def sort_by_price_high_to_low(self):
        self.page.select_option(self.sort_dropdown, "hilo")

    def add_backpack_to_cart(self):
        self.page.click("[data-test='add-to-cart-sauce-labs-backpack']")

    def remove_backpack_from_cart(self):
        self.page.click("[data-test='remove-sauce-labs-backpack']")

    def add_bike_light_to_cart(self):
        self.page.click("[data-test='add-to-cart-sauce-labs-bike-light']")

    def add_all_products_to_cart(self):
        add_buttons = self.page.locator("button[data-test^='add-to-cart']")
        count = add_buttons.count()

        for _ in range(count):
            add_buttons.first.click()

    def get_cart_badge_count(self):
        return self.page.locator(self.cart_badge).inner_text()

    def is_backpack_remove_button_visible(self):
        return self.page.locator("[data-test='remove-sauce-labs-backpack']").is_visible()

    def open_backpack_detail_by_name(self):
        self.page.click("[data-test='item-4-title-link']")

    def open_backpack_detail_by_image(self):
        self.page.click("#item_4_img_link")

    def open_cart(self):
        self.page.click(self.cart_link)