class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"
        self.error_message = "[data-test='error']"
        self.inventory_container = ".inventory_list"

    def navigate(self, url):
        self.page.goto(url)

    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def get_error_message(self):
        return self.page.locator(self.error_message).inner_text()

    def is_error_message_visible(self):
        return self.page.locator(self.error_message).is_visible()

    def is_inventory_page_loaded(self):
        return self.page.locator(self.inventory_container).is_visible()