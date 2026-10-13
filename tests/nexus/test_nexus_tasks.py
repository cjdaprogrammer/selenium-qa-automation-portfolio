from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from uuid import uuid4

from selenium.common.exceptions import (
    StaleElementReferenceException,
    TimeoutException,
)

def click_when_ready(driver, locator, timeout=20):
    """Retry locating and clicking an element if the page re-renders."""
    wait = WebDriverWait(driver, timeout)

    def try_click(browser):
        try:
            element = browser.find_element(*locator)

            if element.is_displayed() and element.is_enabled():
                element.click()
                return True

            return False

        except StaleElementReferenceException:
            return False

    wait.until(try_click)

def test_add_task(driver):
    """Verify that a user can create a task in NEXUS."""

    wait = WebDriverWait(driver, 20)
    task_name = f"Selenium Automation Task {uuid4().hex[:8]}"

    driver.get("https://nexus-personalos.vercel.app/")

    click_when_ready(
        driver,
        (By.XPATH, "//button[normalize-space()='Add Task']")
    )
    title_input = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='Build the authentication system']")
        )
    )
    title_input.send_keys(task_name)

    dropdowns = wait.until(
        EC.visibility_of_all_elements_located(
            (By.TAG_NAME, "select")
        )
    )

    assert len(dropdowns) >= 2, "Task form dropdowns were not found"

    Select(dropdowns[0]).select_by_visible_text("Personal")
    Select(dropdowns[1]).select_by_visible_text("Medium")

    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Create Task']")
        )
    ).click()

    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, f"//*[normalize-space()='{task_name}']")
        )
    )

    assert task_name in driver.find_element(
        By.TAG_NAME, "body"
    ).text

