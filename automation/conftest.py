import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

# Note: Using conftest.py to initialize our page objects 
# keeps our actual test files incredibly clean and focused on business logic.

@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)

@pytest.fixture
def inventory_page(page: Page):
    return InventoryPage(page)

@pytest.fixture
def cart_page(page: Page):
    return CartPage(page)