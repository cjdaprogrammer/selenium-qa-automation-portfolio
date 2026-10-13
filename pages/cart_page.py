from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    PRODUCT_QUANTITIES = (By.CLASS_NAME, "cart_quantity")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def wait_until_loaded(self):
        self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "cart_contents_container")
            )
        )
        return self

    def get_product_names(self):
        """Return product names, or an empty list if the cart is empty."""
        elements = self.driver.find_elements(*self.PRODUCT_NAMES)
        return [element.text for element in elements]

    def get_product_prices(self):
        """Return cart product prices as floats."""
        elements = self.wait.until(
            EC.visibility_of_all_elements_located(
                self.PRODUCT_PRICES
            )
        )
        return [
            float(element.text.replace("$", ""))
            for element in elements
        ]

    def get_product_quantities(self):
        """Return cart product quantities as integers."""
        elements = self.wait.until(
            EC.visibility_of_all_elements_located(
                self.PRODUCT_QUANTITIES
            )
        )
        return [int(element.text) for element in elements]

    def get_cart_items(self):
        """Return all product rows currently in the cart."""
        return self.driver.find_elements(*self.CART_ITEMS)

    def get_cart_item_count(self):
        """Return the number of product rows in the cart."""
        return len(self.get_cart_items())

    def is_product_in_cart(self, product_name):
        """Check whether a specific product is in the cart."""
        return product_name in self.get_product_names()

    def remove_backpack(self):
        """Remove the Sauce Labs Backpack from the cart."""
        locator = (By.ID, "remove-sauce-labs-backpack")
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()
        return self

    def proceed_to_checkout(self):
        """Click the checkout button."""
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()
        return self