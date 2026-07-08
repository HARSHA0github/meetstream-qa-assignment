from playwright.sync_api import expect

def test_saucedemo_cart_flow(page, login_page, inventory_page, cart_page):
    """
    End-to-end test covering login, cart manipulation, and logout.
    Validates dynamic badge updates and item retention.
    """
    # 1. Launch browser & Navigate
    login_page.navigate()

    # 2. Login
    login_page.login("standard_user", "secret_sauce")

    # 3. Add two products to cart
    item_1 = "sauce labs backpack"
    item_2 = "sauce labs bike light"
    inventory_page.add_item_to_cart(item_1)
    inventory_page.add_item_to_cart(item_2)

    # 4. Verify cart badge displays 2
    inventory_page.verify_cart_badge_count("2")

    # 5. Navigate to the cart
    inventory_page.go_to_cart()

    # 6. Verify both selected products are present
    cart_page.verify_item_in_cart("Sauce Labs Backpack")
    cart_page.verify_item_in_cart("Sauce Labs Bike Light")

    # 7. Remove one product
    cart_page.remove_item(item_1)

    # 8. Verify the cart badge updates to 1
    # Note: We check the badge from the inventory_page object because 
    # it exists in the top nav bar, which is shared across pages.
    inventory_page.verify_cart_badge_count("1")

    # 9. Continue shopping
    cart_page.continue_shopping()

    # 10. Add another product
    item_3 = "sauce labs bolt t-shirt"
    inventory_page.add_item_to_cart(item_3)

    # 11. Verify the cart badge displays 2 again
    inventory_page.verify_cart_badge_count("2")

    # 12. Logout successfully
    inventory_page.logout()
    
    # Final assertion to ensure we actually landed back on the login screen
    expect(login_page.login_button).to_be_visible()