from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    # Checkout information form
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    # Checkout overview
    FINISH_BUTTON = (By.ID, "finish")
    SUMMARY = (By.CLASS_NAME, "checkout_summary_container")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")

    # Checkout confirmation and validation
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    CONFIRMATION = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def enter_customer_details(
        self, first_name, last_name, postal_code
    ):
        """Enter customer information into the checkout form."""
        fields = (
            (self.FIRST_NAME, first_name),
            (self.LAST_NAME, last_name),
            (self.POSTAL_CODE, postal_code),
        )

        for locator, value in fields:
            field = self.wait.until(
                EC.visibility_of_element_located(locator)
            )
            field.clear()

            if value:
                field.send_keys(value)

    def continue_checkout(self):
        """Submit customer information and wait for the response."""
        button = self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        )
        button.click()

        # Wait until either validation appears or the overview loads.
        self.wait.until(
            lambda driver: (
                driver.find_elements(*self.ERROR_MESSAGE)
                and driver.find_element(
                    *self.ERROR_MESSAGE
                ).is_displayed()
            )
            or driver.find_elements(*self.SUMMARY)
        )

    def get_error_message(self):
        """Return the visible checkout validation message."""
        error = self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )
        return error.text.strip()

    def get_product_names(self):
        """Return product names displayed in checkout overview."""
        self.wait.until(
            EC.visibility_of_element_located(self.SUMMARY)
        )

        return [
            element.text
            for element in self.driver.find_elements(
                *self.PRODUCT_NAMES
            )
        ]

    def finish_checkout(self):
        """Complete the purchase."""
        button = self.wait.until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)
        )
        button.click()

    def get_confirmation(self):
        """Return the order confirmation message."""
        confirmation = self.wait.until(
            EC.visibility_of_element_located(self.CONFIRMATION)
        )
        return confirmation.text.strip()