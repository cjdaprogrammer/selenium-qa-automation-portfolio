
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    SUMMARY = (By.CLASS_NAME, "checkout_summary_container")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CONFIRMATION = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def enter_customer_details(self, first_name, last_name, postal_code):
        for locator, value in (
            (self.FIRST_NAME, first_name),
            (self.LAST_NAME, last_name),
            (self.POSTAL_CODE, postal_code),
        ):
            field = self.wait.until(
                EC.visibility_of_element_located(locator)
            )
            field.clear()
            if value:
                field.send_keys(value)

    def continue_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        ).click()

    def get_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        ).text

    def get_product_names(self):
        self.wait.until(
            EC.visibility_of_element_located(self.SUMMARY)
        )
        return [
            element.text
            for element in self.driver.find_elements(*self.PRODUCT_NAMES)
        ]

    def finish_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)
        ).click()

    def get_confirmation(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.CONFIRMATION)
        ).text
