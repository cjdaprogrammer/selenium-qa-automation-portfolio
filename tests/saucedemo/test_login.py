from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_valid_login(driver):
    """Verify that valid credentials allow login."""
    LoginPage(driver).open().login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver).wait_until_loaded()

    assert "/inventory.html" in driver.current_url
    assert inventory.get_products()


def test_invalid_login(driver):
    """Verify that incorrect credentials display an error."""
    login_page = LoginPage(driver).open()
    login_page.login("wrong_user", "wrong_password")

    error = login_page.get_error_message()

    assert "Username and password do not match" in error


def test_empty_login(driver):
    """Verify that submitting empty fields displays an error."""
    login_page = LoginPage(driver).open()
    login_page.login("", "")

    error = login_page.get_error_message()

    assert "Username is required" in error


def test_products_are_displayed(driver):
    """Verify that products appear after successful login."""
    LoginPage(driver).open().login("standard_user", "secret_sauce")

    products = InventoryPage(driver).wait_until_loaded().get_products()

    assert len(products) > 0
    print(f"\nProducts displayed: {len(products)}")


def test_add_product_to_cart(driver):
    """Verify that adding a product updates the cart count."""
    LoginPage(driver).open().login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver).wait_until_loaded()
    inventory.add_backpack_to_cart()

    assert inventory.get_cart_count() == "1"


def test_cart_contains_correct_product(driver):
    """Verify that the selected product appears in the cart."""
    LoginPage(driver).open().login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver).wait_until_loaded()
    inventory.add_backpack_to_cart()
    inventory.open_cart()

    from pages.cart_page import CartPage

    cart = CartPage(driver)

    assert "Sauce Labs Backpack" in cart.get_product_names()
    assert "/cart.html" in driver.current_url


def test_locked_out_user_cannot_login(driver):
    """Verify that a locked-out account cannot access inventory."""
    login_page = LoginPage(driver).open()
    login_page.login("locked_out_user", "secret_sauce")

    error = login_page.get_error_message()

    assert "locked out" in error.lower()
    assert "/inventory.html" not in driver.current_url

def test_products_can_be_sorted_by_price_low_to_high(driver):
    """Verify products are sorted from lowest to highest price."""
    LoginPage(driver).open().login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver).wait_until_loaded()
    inventory.sort_by_price_low_to_high()

    prices = inventory.get_product_prices()

    assert len(prices) > 1
    assert prices == sorted(prices), (
        f"Products are not sorted by ascending price: {prices}"
    )