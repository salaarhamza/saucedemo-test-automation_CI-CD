class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.first_name_input = "[data-test='firstName']"
        self.last_name_input = "[data-test='lastName']"
        self.postal_code_input = "[data-test='postalCode']"
        self.continue_button = "[data-test='continue']"
        self.finish_button = "[data-test='finish']"
        self.error_message = "[data-test='error']"
        self.complete_header = ".complete-header"

    def fill_checkout_information(self, first_name, last_name, postal_code):
        self.page.fill(self.first_name_input, first_name)
        self.page.fill(self.last_name_input, last_name)
        self.page.fill(self.postal_code_input, postal_code)

    def continue_checkout(self):
        self.page.click(self.continue_button)

    def finish_checkout(self):
        self.page.click(self.finish_button)

    def complete_order(self, first_name, last_name, postal_code):
        self.fill_checkout_information(first_name, last_name, postal_code)
        self.continue_checkout()
        self.finish_checkout()

    def get_error_message(self):
        return self.page.locator(self.error_message).inner_text()

    def is_checkout_complete(self):
        return self.page.locator(self.complete_header).is_visible()

    def get_complete_message(self):
        return self.page.locator(self.complete_header).inner_text()

    def cancel_checkout(self):
        self.page.click("[data-test='cancel']")

    def get_overview_item_names(self):
        return self.page.locator(".inventory_item_name").all_inner_texts()

    def get_item_total(self):
        text = self.page.locator(".summary_subtotal_label").inner_text()
        return float(text.replace("Item total: $", ""))

    def get_tax(self):
        text = self.page.locator(".summary_tax_label").inner_text()
        return float(text.replace("Tax: $", ""))

    def get_total(self):
        text = self.page.locator(".summary_total_label").inner_text()
        return float(text.replace("Total: $", ""))

    def back_home(self):
        self.page.click("[data-test='back-to-products']")