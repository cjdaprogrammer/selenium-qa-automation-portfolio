
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException


NEXUS_URL = "https://nexus-personalos.vercel.app/"


def open_nexus(driver):
    """Open NEXUS and return an explicit wait."""
    driver.get(NEXUS_URL)
    wait = WebDriverWait(driver, 30)

    wait.until(
        lambda browser: browser.execute_script(
            "return document.readyState"
        ) == "complete"
    )

    return wait


def click_fresh_element(driver, locator, timeout=30):
    """Re-find an element whenever a page re-render makes it stale."""
    wait = WebDriverWait(driver, timeout)

    def attempt_click(browser):
        try:
            element = browser.find_element(*locator)

            if element.is_displayed() and element.is_enabled():
                element.click()
                return True

            return False

        except StaleElementReferenceException:
            return False

    wait.until(attempt_click)


def test_nexus_dashboard_loads(driver):
    """Verify the NEXUS dashboard loads."""
    open_nexus(driver)

    wait = WebDriverWait(driver, 30)
    wait.until(
        lambda browser: len(browser.find_elements(By.TAG_NAME, "body")) > 0
    )

    assert "NEXUS" in driver.page_source.upper()


def test_nexus_navigation_pages(driver):
    """Verify main navigation items can be selected."""
    wait = open_nexus(driver)

    pages = [
        "Dashboard",
        "Goals",
        "Projects",
        "Habits",
        "Skills",
        "Knowledge",
    ]

    for page in pages:
        locator = (
            By.XPATH,
            f"//button[normalize-space()='{page}']",
        )

        click_fresh_element(driver, locator)

        # Wait for the app to finish updating after navigation.
        wait.until(
            lambda browser: browser.execute_script(
                "return document.readyState"
            ) == "complete"
        )

        assert page.lower() in driver.page_source.lower(), (
            f"Expected '{page}' to appear after selecting that navigation item."
        )


def test_nexus_add_task_form_opens(driver):
    """Verify the Add Task form opens and displays its title field."""
    open_nexus(driver)

    add_task_button = (
        By.XPATH,
        "//button[normalize-space()='Add Task']",
    )

    click_fresh_element(driver, add_task_button)

    title_field = (
        By.XPATH,
        "//input[@placeholder='Build the authentication system']",
    )

    WebDriverWait(driver, 30).until(
        lambda browser: any(
            element.is_displayed()
            for element in browser.find_elements(*title_field)
        )
    )
