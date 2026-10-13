
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    URL = "https://www.saucedemo.com/"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self):
        self.driver.get(self.URL)
        self.wait.until(
            EC.visibility_of_element_located(self.USERNAME)
        )
        return self

    def login(self, username, password):
        username_field = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME)
        )
        username_field.clear()
        username_field.send_keys(username)

        password_field = self.driver.find_element(*self.PASSWORD)
        password_field.clear()
        password_field.send_keys(password)

        self.driver.find_element(*self.LOGIN_BUTTON).click()
        return self

    def get_error_message(self):
        error = self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )
        return error.text
