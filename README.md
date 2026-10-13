# Selenium QA Automation Portfolio

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green?logo=selenium&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Testing-blue?logo=pytest&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF?logo=githubactions&logoColor=white)

**An automated software testing project demonstrating functional testing, regression testing, Page Object Model design, and continuous integration using Selenium WebDriver and pytest.**

[View Repository](https://github.com/cjdaprogrammer/selenium-qa-automation-portfolio) · [View Test Workflow](https://github.com/cjdaprogrammer/selenium-qa-automation-portfolio/actions)

## Project Overview

This project demonstrates practical QA automation skills through automated tests for two applications: SauceDemo and NEXUS.

The test suite validates important application behavior, including login functionality, inventory display, shopping cart operations, checkout workflows, form validation, navigation, and task creation.

The framework is designed to be maintainable, reusable, and suitable for running locally and in a continuous integration environment.

## Test Results

| Metric | Result |
|---|---|
| Total automated tests | 17 |
| Local test execution | 17 passed |
| GitHub Actions execution | 17 passed |
| Latest recorded CI execution time | 23.11 seconds |
| Automated test framework | pytest |
| Browser automation | Selenium WebDriver |

*Results reflect the successful test runs recorded during project development. Test results may change when the code or test environment changes.*

## Technologies Used

- **Python 3.11** — programming language for the automation framework.
- **Selenium WebDriver** — browser automation and UI interaction.
- **pytest** — test execution, fixtures, assertions, and test organization.
- **pytest-html** — HTML test report generation.
- **Page Object Model (POM)** — separates page interactions from test logic.
- **Git and GitHub** — source control and project hosting.
- **GitHub Actions** — automated test execution in a Linux CI environment.
- **Microsoft Edge and Google Chrome** — local and CI browser testing.

## Test Coverage

### 1. SauceDemo — Login and Inventory

The automated tests cover:

- Successful login with valid credentials.
- Rejection of invalid credentials.
- Validation of empty login fields.
- Display of inventory products.
- Adding a product to the shopping cart.
- Verifying the correct product in the cart.
- Preventing login for a locked-out user.
- Sorting products by price from low to high.

### 2. SauceDemo — Cart and Checkout

The automated tests cover:

- Removing a product from the shopping cart.
- Completing the checkout process.
- Validating a missing first name.
- Validating a missing last name.
- Validating a missing postal code.

### 3. NEXUS — Dashboard and Tasks

The automated tests cover:

- Dashboard loading.
- Navigation between application pages.
- Opening the add-task form.
- Adding a task.

## Project Structure

```text
selenium-qa-automation-portfolio/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── nexus/
│   │   ├── test_nexus.py
│   │   └── test_nexus_tasks.py
│   │
│   └── saucedemo/
│       ├── test_login.py
│       └── test_checkout.py
│
├── reports/
│   ├── report.html
│   └── screenshots/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

*The structure above reflects the main project files; generated report and screenshot files may vary depending on your local setup and `.gitignore` rules.*

## Getting Started

### Prerequisites

Install the following:

- Python 3.11 or a compatible Python 3 version.
- Git.
- Microsoft Edge for local execution, or Google Chrome if you configure the framework to use Chrome.
- A working internet connection to access the applications under test.

### 1. Clone the repository

```bash
git clone https://github.com/cjdaprogrammer/selenium-qa-automation-portfolio.git
cd selenium-qa-automation-portfolio
```

### 2. Create a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell prevents activation, you can run the Python executable inside `.venv` directly or use another supported activation method.

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the complete test suite

```bash
python -m pytest -v
```

### 5. Generate an HTML test report

```bash
python -m pytest -v --html=reports/report.html --self-contained-html
```

Open the generated report on Windows:

```powershell
Start-Process reports/report.html
```

The report includes the results of the test run. Its contents are generated each time pytest executes.

## Continuous Integration

The project uses GitHub Actions to run automated tests when changes are pushed to the configured branches, when pull requests target those branches, or when the workflow is manually triggered.

The workflow:

1. Checks out the repository.
2. Sets up Python.
3. Installs Chrome.
4. Installs the Python dependencies.
5. Checks the Chrome installation and removes a conflicting system ChromeDriver when necessary.
6. Runs the pytest suite in headless Chrome.
7. Generates an HTML report.
8. Uploads the report and available failure screenshots as workflow artifacts.

View workflow runs and execution results:

**[GitHub Actions — Selenium QA Automation](https://github.com/cjdaprogrammer/selenium-qa-automation-portfolio/actions)**

## QA Skills Demonstrated

This project demonstrates experience with:

- Writing and executing automated test cases.
- Positive and negative test scenarios.
- UI functional and regression testing.
- Form validation and error-message verification.
- Browser automation and explicit waits.
- Reusable page objects and pytest fixtures.
- Assertions and automated test reporting.
- Failure screenshots and troubleshooting.
- Version control with Git.
- Continuous integration using GitHub Actions.
- Debugging differences between local and CI environments.

## Future Improvements

Potential enhancements include:

- Expand test coverage for additional user journeys.
- Add more negative and boundary-value scenarios.
- Improve test data management and configuration.
- Add structured logging and clearer failure diagnostics.
- Add cross-browser CI testing.
- Document test cases and defect reports separately.
- Improve execution speed and test isolation.

## Author

**Junior QA Engineer Portfolio Project**

GitHub: [@cjdaprogrammer](https://github.com/cjdaprogrammer)

This project was created to demonstrate practical skills in software quality assurance, UI automation, test design, debugging, and continuous integration.