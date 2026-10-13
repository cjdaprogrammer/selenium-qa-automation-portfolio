import os
from pathlib import Path

import pytest
from selenium import webdriver


PROJECT_ROOT = Path(__file__).resolve().parent
SCREENSHOT_DIR = PROJECT_ROOT / "reports" / "screenshots"


@pytest.fixture
def driver(request):
    """Use Edge locally or Chrome in CI; capture test failures."""
    browser_name = os.getenv("SELENIUM_BROWSER", "edge").lower()

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()

        # Use the Chrome binary configured in GitHub Actions, if provided.
        chrome_bin = os.getenv("CHROME_BIN")
        if chrome_bin:
            options.binary_location = chrome_bin

        # Headless settings for GitHub Actions.
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

        # Selenium Manager locates a compatible ChromeDriver.
        browser = webdriver.Chrome(options=options)

    elif browser_name == "edge":
        browser = webdriver.Edge()
        browser.maximize_window()

    else:
        raise ValueError(
            f"Unsupported SELENIUM_BROWSER: {browser_name}"
        )

    try:
        yield browser

    finally:
        # Save a screenshot when the test call fails.
        report = getattr(request.node, "rep_call", None)

        if report is not None and report.failed:
            try:
                SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

                safe_name = "".join(
                    character
                    if character.isalnum() or character in "-_"
                    else "_"
                    for character in request.node.nodeid
                )

                screenshot_path = SCREENSHOT_DIR / f"{safe_name}.png"

                if browser.save_screenshot(str(screenshot_path)):
                    print(
                        f"\nFailure screenshot saved: {screenshot_path}"
                    )

            except Exception as error:
                print(f"\nCould not save screenshot: {error}")

        browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Make test results available to fixtures."""
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)
