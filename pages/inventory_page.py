from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def wait_until_loaded(self):
        self.wait.until(
            EC.visibility_of_element_located(self.INVENTORY_LIST)
        )
        return self

    def get_products(self):
        return self.wait.until(
            EC.visibility_of_all_elements_located(self.INVENTORY_ITEMS)
        )

    def add_backpack_to_cart(self):
        button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.wait.until(
            EC.element_to_be_clickable(button)
        ).click()
        return self

    def get_cart_count(self):
        badge = self.wait.until(
            EC.visibility_of_element_located(self.CART_BADGE)
        )
        return badge.text

    def open_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        ).click()
        return self

    def sort_by_price_low_to_high(self):
        """Sort products from lowest price to highest price."""
        dropdown = self.wait.until(
            EC.element_to_be_clickable(self.SORT_DROPDOWN)
        )
        Select(dropdown).select_by_value("lohi")
        return self

    def get_product_prices(self):
        """Return product prices as numeric values."""
        price_elements = self.wait.until(
            EC.visibility_of_all_elements_located(self.PRODUCT_PRICES)
        )
        return [
            float(element.text.replace("$", ""))
            for element in price_elements
        ]
