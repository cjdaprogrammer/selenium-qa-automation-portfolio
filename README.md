# Selenium QA Automation Portfolio

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green)
![Pytest](https://img.shields.io/badge/Pytest-19%20Tests-orange)
![GitHub Actions](https://github.com/cjdaprogrammer/selenium-qa-automation-portfolio/actions/workflows/tests.yml/badge.svg)

A practical QA automation portfolio demonstrating functional testing, regression testing, the Page Object Model (POM), automated test reporting, failure screenshots, and continuous integration using Selenium WebDriver and pytest.

**Applications tested:** SauceDemo and NEXUS.

## Project Overview

This project demonstrates how automated UI tests can validate application behavior, verify expected results, and help detect regressions.

The framework includes reusable page objects, explicit waits, pytest fixtures, HTML test reports, screenshots on test failures, and GitHub Actions for continuous integration.

## Test Results

| Metric | Result |
|---|---|
| Automated test cases | 19 |
| Latest local execution | 19 passed |
| Latest GitHub Actions execution | 19 passed |
| Local browser | Microsoft Edge |
| CI browser | Google Chrome |
| Test framework | pytest |
| Automation tool | Selenium WebDriver |

*Results reflect the latest executions verified during project development. Future code changes may affect test results.*

## Test Coverage

### SauceDemo

The automated tests cover:

- Valid login
- Invalid login
- Empty login validation
- Username and password required-field validation
- Locked-out user validation
- Product inventory display
- Adding a product to the cart
- Verifying the correct cart product
- Sorting products by price, low to high
- Removing a product from the cart
- Completing checkout
- Checkout required-field validation for first name, last name, and postal code

### NEXUS

The automated tests cover:

- Dashboard loading
- Navigation between application pages
- Add-task form visibility
- Adding a task

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
selenium-qa-automation-portfolio/
├── .github/
│   └── workflows/
│       └── tests.yml
├── docs/
│   ├── test-plan.md
│   ├── manual-test-cases.md
│   ├── bug-report.md
│   └── requirements-traceability-matrix.md
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── nexus/
│   │   ├── test_nexus.py
│   │   └── test_nexus_tasks.py
│   └── saucedemo/
│       ├── test_login.py
│       └── test_checkout.py
├── reports/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.11 or a compatible Python 3 version
- Git
- Microsoft Edge or Google Chrome
- Internet access to load the demo applications and install dependencies

Selenium Manager can automatically manage compatible browser drivers in supported environments.

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

For Windows Command Prompt:

```bat
.venv\Scripts\activate.bat
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the automated test suite

```bash
python -m pytest tests -v
```

### 5. Generate an HTML report

Ensure the `reports` directory exists, then run:

```bash
python -m pytest tests -v --html=reports/report.html --self-contained-html
```

Open the report in Windows PowerShell:

```powershell
Start-Process reports/report.html
```

The HTML report records the results of that particular test execution.

## Continuous Integration

GitHub Actions runs the automated test suite according to the configured workflow triggers.

The workflow is designed to:

1. Check out the repository.
2. Set up Python.
3. Install the required dependencies and browser components.
4. Execute the pytest suite.
5. Generate an HTML test report.
6. Upload reports as workflow artifacts when configured.

**Latest verified result:** 19 tests passed in GitHub Actions.

[View GitHub Actions workflow runs](https://github.com/cjdaprogrammer/selenium-qa-automation-portfolio/actions)

## QA Practices Demonstrated

- Positive and negative test scenarios
- Required-field validation
- Assertions and expected-result verification
- Reusable Page Object Model classes
- Explicit waits for UI synchronization
- pytest fixtures and browser cleanup
- Automated HTML test reporting
- Screenshots on test failures
- Continuous integration with GitHub Actions
- Browser and driver compatibility troubleshooting
- Manual test documentation
- Requirements traceability
- Structured defect reporting

## QA Documentation

| Document | Description |
|---|---|
| [Test Plan](docs/test-plan.md) | Defines testing objectives, scope, environment, approach, and exit criteria. |
| [Manual Test Cases](docs/manual-test-cases.md) | Documents manual test scenarios for SauceDemo and NEXUS. |
| [Bug Report](docs/bug-report.md) | Provides defect-reporting documentation and a clearly labeled hypothetical example. |
| [Requirements Traceability Matrix](docs/requirements-traceability-matrix.md) | Maps requirements to test cases and automation scripts. |

## Skills Demonstrated

- Test case design and organization
- Functional and negative testing
- UI automation using Selenium WebDriver
- Python test automation with pytest
- Test execution and result reporting
- Defect documentation
- Requirements traceability
- Continuous integration using GitHub Actions
- Debugging and troubleshooting automated tests

## Future Improvements

- Add API testing with pytest and HTTPX
- Expand boundary-value and negative testing
- Introduce test data management
- Add structured logging
- Expand cross-browser coverage
- Improve test isolation and execution speed
- Add further regression scenarios and reporting metrics

## Author

**Junior QA Engineer Portfolio Project**

GitHub: [@cjdaprogrammer](https://github.com/cjdaprogrammer)

This project was created to demonstrate practical software quality assurance skills, UI test automation, test design, debugging, documentation, and continuous integration.
