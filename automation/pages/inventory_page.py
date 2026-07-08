from playwright.sync_api import expect

class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")
        self.burger_menu = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator("#logout_sidebar_link")

    def add_item_to_cart(self, item_name):
        # Dynamically targets the add-to-cart button based on the item name
        # Using string replacement to match SauceDemo's locator pattern
        formatted_name = item_name.lower().replace(" ", "-")
        locator_string = f"[data-test='add-to-cart-{formatted_name}']"
        self.page.locator(locator_string).click()

    def verify_cart_badge_count(self, expected_count):
        if expected_count == "0" or expected_count == 0:
            expect(self.cart_badge).to_be_hidden()
        else:
            expect(self.cart_badge).to_have_text(str(expected_count))

    def go_to_cart(self):
        self.cart_link.click()

    def logout(self):
        self.burger_menu.click()
        # Playwright's auto-wait handles the side menu animation delay perfectly here
        self.logout_link.click()