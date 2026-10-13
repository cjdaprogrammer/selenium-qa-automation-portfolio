# Selenium QA Automation Portfolio

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green)
![Pytest](https://img.shields.io/badge/Pytest-Testing-orange)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-success)

A practical QA automation portfolio demonstrating functional testing, regression testing, Page Object Model (POM) design, automated test reporting, failure screenshots, and continuous integration using Selenium WebDriver and pytest.

**Applications tested:** SauceDemo and NEXUS.

## Project Overview

This project demonstrates how automated UI tests can validate essential application behavior, identify regressions, and provide repeatable test results.

The framework uses reusable page objects, explicit waits, pytest fixtures, HTML reports, failure screenshots, and GitHub Actions to support maintainable automated testing.

## Test Results

| Metric | Result |
|---|---|
| Automated test cases | 17 |
| Local test execution | 17 passed |
| GitHub Actions execution | 17 passed |
| Local browser | Microsoft Edge |
| CI browser | Google Chrome |
| Test framework | pytest |
| Automation tool | Selenium WebDriver |

*These results reflect successful executions completed during project development. Rerun the suite to verify the current results after subsequent changes.*

## Test Coverage

### SauceDemo

- Valid login
- Invalid login
- Empty login validation
- Locked-out user validation
- Product inventory display
- Add a product to the cart
- Verify cart contents
- Sort products by price
- Remove a product from the cart
- Complete checkout
- Validate required checkout fields

### NEXUS

- Dashboard loading
- Navigation between application pages
- Add-task form visibility
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

*This tree represents the intended project layout. Keep it synchronized with the files actually present in the repository.*

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

If you're using Command Prompt instead:

```bat
.venv\Scripts\activate.bat
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

Ensure the required browser is installed. Selenium Manager can help manage the browser driver.

### 4. Run the automated test suite

```bash
python -m pytest -v
```

### 5. Generate an HTML test report

```bash
python -m pytest -v --html=reports/report.html --self-contained-html
```

Open the generated report in Windows PowerShell:

```powershell
Start-Process reports/report.html
```

The report contains the execution results from that run. If the `reports` directory does not exist, create it before running the report command.

## Continuous Integration

GitHub Actions automates test execution when changes are pushed to configured branches or a pull request is opened, according to the workflow configuration.

The workflow is designed to:

1. Check out the repository.
2. Set up Python.
3. Install the required browser and project dependencies.
4. Execute the pytest suite.
5. Generate an HTML test report.
6. Upload test reports as workflow artifacts, if configured.

View the [GitHub Actions workflow runs](https://github.com/cjdaprogrammer/selenium-qa-automation-portfolio/actions).

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

The following documents demonstrate practical QA documentation skills and support the testing activities in this portfolio.

| Document | Description |
|---|---|
| [Test Plan](docs/test-plan.md) | Defines testing objectives, scope, environment, approach, and exit criteria. |
| [Manual Test Cases](docs/manual-test-cases.md) | Documents manual test scenarios for SauceDemo and NEXUS. |
| [Bug Report](docs/bug-report.md) | Provides a defect-reporting template and a clearly labeled hypothetical example. |
| [Requirements Traceability Matrix](docs/requirements-traceability-matrix.md) | Maps requirements to test cases and automation scripts. |

### Testing Skills

- Writing and organizing test cases
- Functional and negative testing
- UI test automation using Selenium WebDriver
- Test execution and result reporting
- Defect documentation
- Requirements traceability
- Continuous integration using GitHub Actions

## Future Improvements

- Add API testing
- Expand boundary-value and negative testing
- Introduce test data management
- Add structured logging
- Expand cross-browser testing
- Improve test isolation and execution speed
- Add verified defect examples and regression scenarios
- Expand reporting and test coverage metrics

## Author

**Junior QA Engineer Portfolio Project**

GitHub: [@cjdaprogrammer](https://github.com/cjdaprogrammer)

This project was created to demonstrate practical skills in software quality assurance, UI automation, test design, debugging, test documentation, and continuous integration.
