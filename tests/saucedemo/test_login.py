import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.mark.smoke
def test_valid_login(driver):
    """Verify that valid credentials allow login."""
    LoginPage(driver).open().login(
        "standard_user",
        "secret_sauce",
    )

    inventory = InventoryPage(driver).wait_until_loaded()

    assert "/inventory.html" in driver.current_url
    assert len(inventory.get_products()) > 0


@pytest.mark.smoke
def test_invalid_login(driver):
    """Verify that incorrect credentials display an error."""
    login_page = LoginPage(driver).open()
    login_page.login("wrong_user", "wrong_password")

    error = login_page.get_error_message()

    assert "Username and password do not match" in error
    assert "/inventory.html" not in driver.current_url


def test_empty_login(driver):
    """Verify that empty credentials are rejected."""
    login_page = LoginPage(driver).open()
    login_page.login("", "")

    assert "Username is required" in login_page.get_error_message()


def test_username_required(driver):
    """Verify that a password without a username is rejected."""
    login_page = LoginPage(driver).open()
    login_page.login("", "secret_sauce")

    assert "Username is required" in login_page.get_error_message()


def test_password_required(driver):
    """Verify that a username without a password is rejected."""
    login_page = LoginPage(driver).open()
    login_page.login("standard_user", "")

    assert "Password is required" in login_page.get_error_message()


def test_locked_out_user_cannot_login(driver):
    """Verify that a locked-out account cannot access inventory."""
    login_page = LoginPage(driver).open()
    login_page.login("locked_out_user", "secret_sauce")

    assert "locked out" in login_page.get_error_message().lower()
    assert "/inventory.html" not in driver.current_url


def test_products_are_displayed(driver):
    """Verify that products appear after successful login."""
    LoginPage(driver).open().login(
        "standard_user",
        "secret_sauce",
    )

    products = InventoryPage(driver).wait_until_loaded().get_products()

    assert len(products) > 0
    print(f"\nProducts displayed: {len(products)}")


def test_add_product_to_cart(driver):
    """Verify that adding a product updates the cart count."""
    LoginPage(driver).open().login(
        "standard_user",
        "secret_sauce",
    )

    inventory = InventoryPage(driver).wait_until_loaded()
    inventory.add_backpack_to_cart()

    assert inventory.get_cart_count() == "1"



def test_cart_contains_correct_product(driver):
    """Verify the cart displays the correct product, price, and quantity."""
    LoginPage(driver).open().login(
        "standard_user",
        "secret_sauce",
    )

    inventory = InventoryPage(driver).wait_until_loaded()
    inventory.add_backpack_to_cart()
    inventory.open_cart()

    cart = CartPage(driver).wait_until_loaded()

    assert "/cart.html" in driver.current_url
    assert cart.is_product_in_cart("Sauce Labs Backpack")
    assert cart.get_product_prices() == [29.99]
    assert cart.get_product_quantities() == [1]
    assert cart.get_cart_item_count() == 1


def test_products_can_be_sorted_by_price_low_to_high(driver):
    """Verify products are sorted from lowest to highest price."""
    LoginPage(driver).open().login(
        "standard_user",
        "secret_sauce",
    )

    inventory = InventoryPage(driver).wait_until_loaded()
    inventory.sort_by_price_low_to_high()

    prices = inventory.get_product_prices()

    assert len(prices) > 1
    assert prices == sorted(prices), (
        f"Products are not sorted by ascending price: {prices}"
    )
