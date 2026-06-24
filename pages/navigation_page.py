class NavigationPage:
    def __init__(self, page):
        self.page = page
        self.burger_menu_button = "#react-burger-menu-btn"
        self.all_items_link = "#inventory_sidebar_link"
        self.about_link = "#about_sidebar_link"
        self.logout_link = "#logout_sidebar_link"
        self.reset_app_state_link = "#reset_sidebar_link"
        self.cart_badge = ".shopping_cart_badge"
        self.footer_twitter = "[data-test='social-twitter']"
        self.footer_facebook = "[data-test='social-facebook']"
        self.footer_linkedin = "[data-test='social-linkedin']"

    def open_burger_menu(self):
        self.page.click(self.burger_menu_button)

    def click_all_items(self):
        self.open_burger_menu()
        self.page.click(self.all_items_link)

    def get_about_href(self):
        self.open_burger_menu()
        return self.page.locator(self.about_link).get_attribute("href")

    def logout(self):
        self.open_burger_menu()
        self.page.click(self.logout_link)

    def reset_app_state(self):
        self.open_burger_menu()
        self.page.click(self.reset_app_state_link)

    def get_cart_badge_count(self):
        return self.page.locator(self.cart_badge).count()

    def get_footer_link_href(self, social_link):
        return self.page.locator(social_link).get_attribute("href")