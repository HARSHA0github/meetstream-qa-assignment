from playwright.sync_api import expect

class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.continue_shopping_button = page.locator("[data-test='continue-shopping']")

    def verify_item_in_cart(self, item_name):
        # Verifies the exact item text exists within the cart list
        item = self.page.locator(f".inventory_item_name:has-text('{item_name}')")
        expect(item).to_be_visible()

    def remove_item(self, item_name):
        formatted_name = item_name.lower().replace(" ", "-")
        locator_string = f"[data-test='remove-{formatted_name}']"
        self.page.locator(locator_string).click()

    def continue_shopping(self):
        self.continue_shopping_button.click()