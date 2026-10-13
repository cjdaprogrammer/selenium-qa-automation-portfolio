from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def login_and_add_backpack(driver):
    """Prepare a logged-in session with a backpack in the cart."""
    LoginPage(driver).open().login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver).wait_until_loaded()
    inventory.add_backpack_to_cart()
    inventory.open_cart()


def test_remove_product_from_cart(driver):
    """Verify that removing a product leaves the cart empty."""
    login_and_add_backpack(driver)

    cart = CartPage(driver).wait_until_loaded()

    # Confirm the backpack is in the cart before removal.
    assert cart.is_product_in_cart("Sauce Labs Backpack")
    assert cart.get_cart_item_count() == 1

    # Remove the backpack.
    cart.remove_backpack()

    # Verify the product is actually gone.
    assert cart.get_cart_item_count() == 0
    assert not cart.is_product_in_cart("Sauce Labs Backpack")


def test_complete_checkout(driver):
    """Verify that a user can complete a purchase."""
    login_and_add_backpack(driver)

    CartPage(driver).proceed_to_checkout()

    checkout = CheckoutPage(driver)
    checkout.enter_customer_details("Test", "User", "10001")
    checkout.continue_checkout()

    assert "Sauce Labs Backpack" in checkout.get_product_names()

    checkout.finish_checkout()

    assert checkout.get_confirmation() == "Thank you for your order!"


def test_checkout_requires_first_name(driver):
    """Verify that checkout rejects missing first-name information."""
    login_and_add_backpack(driver)

    CartPage(driver).proceed_to_checkout()

    checkout = CheckoutPage(driver)
    checkout.enter_customer_details("", "User", "10001")
    checkout.continue_checkout()

    assert "First Name is required" in checkout.get_error_message()


def test_checkout_requires_last_name(driver):
    """Verify checkout rejects a missing last name."""
    login_and_add_backpack(driver)
    CartPage(driver).proceed_to_checkout()

    checkout = CheckoutPage(driver)
    checkout.enter_customer_details("Test", "", "10001")
    checkout.continue_checkout()

    assert "Last Name is required" in checkout.get_error_message()


def test_checkout_requires_postal_code(driver):
    """Verify checkout rejects a missing postal code."""
    login_and_add_backpack(driver)
    CartPage(driver).proceed_to_checkout()

    checkout = CheckoutPage(driver)
    checkout.enter_customer_details("Test", "User", "")
    checkout.continue_checkout()

    assert "Postal Code is required" in checkout.get_error_message()
