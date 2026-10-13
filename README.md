# Selenium QA Automation Portfolio

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green)
![Pytest](https://img.shields.io/badge/Pytest-Testing-orange)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-success)

A practical QA automation portfolio demonstrating functional testing, regression testing, Page Object Model design, test reporting, failure screenshots, and continuous integration using Selenium WebDriver and pytest.

**Applications tested:** SauceDemo and NEXUS.

## Project Overview

This project demonstrates how automated UI tests can validate essential application behavior, detect regressions, and provide repeatable test results.

The framework uses reusable page objects, explicit waits, pytest fixtures, HTML reports, and GitHub Actions to support maintainable automated testing.

## Test Results

| Metric | Result |
|---|---|
| Automated test cases | 17 |
| Local test execution | 17 passed |
| GitHub Actions execution | 17 passed |
| Browser used locally | Microsoft Edge |
| Browser used in CI | Google Chrome |
| Test framework | pytest |
| Automation tool | Selenium WebDriver |

*Results reflect the successful executions completed during project development.*

## Test Coverage

### SauceDemo
- Valid login
- Invalid login
- Empty login validation
- Locked-out user validation
- Product inventory display
- Add product to cart
- Verify cart contents
- Sort products by price
- Remove a product from the cart
- Complete checkout
- Validate required checkout fields

### NEXUS
- Dashboard loading
- Navigation between application pages
- Task creation form visibility
- Add a task

## Technology Stack

- Python 3.11
- Selenium WebDriver
- pytest
- pytest-html
- Page Object Model (POM)
- GitHub Actions
- Microsoft Edge for local execution
- Google Chrome for CI execution

## Project Structure

```text
test/
├── .github/
│   └── workflows/
│       └── tests.yml
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── nexus/
│   └── saucedemo/
├── reports/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/cjdaprogrammer/selenium-qa-automation-portfolio.git
cd selenium-qa-automation-portfolio
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

Make sure the required browser is installed. Selenium Manager helps manage the browser driver.

### 4. Run the complete test suite

```bash
python -m pytest -v
```

### 5. Generate an HTML test report

```bash
python -m pytest -v --html=reports/report.html --self-contained-html
```

Open the generated report:

```powershell
Start-Process reports/report.html
```

## Continuous Integration

GitHub Actions runs the automated test suite when changes are pushed to the configured branches or a pull request is opened.

The workflow:
1. Checks out the repository.
2. Sets up Python.
3. Installs Chrome and project dependencies.
4. Executes the pytest suite.
5. Generates an HTML report.
6. Uploads test reports as workflow artifacts.

View the [GitHub Actions workflow runs](https://github.com/cjdaprogrammer/selenium-qa-automation-portfolio/actions).

## QA Practices Demonstrated

- Positive and negative test scenarios
- Required-field validation
- Assertions and expected-result verification
- Reusable Page Object Model classes
- Explicit waits for UI synchronization
- pytest fixtures and browser cleanup
- HTML test reporting
- Screenshots on test failures
- Continuous integration with GitHub Actions
- Debugging browser and driver compatibility issues

## Future Improvements

- Add API testing
- Add more boundary-value and negative scenarios
- Add test data management
- Add structured logging
- Expand cross-browser testing
- Improve test isolation and execution speed
- Add more detailed defect reports

## Author

**Junior QA Engineer Portfolio Project**

GitHub: [@cjdaprogrammer](https://github.com/cjdaprogrammer)

This project was created to demonstrate practical skills in software quality assurance, UI automation, test design, debugging, and continuous integration.
