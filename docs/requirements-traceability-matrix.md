# Requirements Traceability Matrix (RTM)

## 1. Document Information

| Field | Details |
|---|---|
| Project | Selenium QA Automation Portfolio |
| Document Type | Requirements Traceability Matrix |
| Version | 1.0 |
| Purpose | Map application requirements to test cases and automated test scripts |

## 2. Traceability Matrix

| Requirement ID | Application | Requirement | Test Case ID | Test Script | Coverage Status |
|---|---|---|---|---|---|
| REQ-SD-001 | SauceDemo | Users can log in with valid credentials | TC-SD-001 | `tests/saucedemo/test_login.py::test_valid_login` | Verify against current test suite |
| REQ-SD-002 | SauceDemo | Invalid credentials display an error | TC-SD-002 | `tests/saucedemo/test_login.py::test_invalid_login` | Verify against current test suite |
| REQ-SD-003 | SauceDemo | Empty login fields are validated | TC-SD-003 | `tests/saucedemo/test_login.py::test_empty_login` | Verify against current test suite |
| REQ-SD-004 | SauceDemo | Inventory products are displayed after login | TC-SD-004 | `tests/saucedemo/test_login.py::test_products_are_displayed` | Verify against current test suite |
| REQ-SD-005 | SauceDemo | Products can be added to the cart | TC-SD-005 | `tests/saucedemo/test_login.py::test_add_product_to_cart` | Confirm test name in source |
| REQ-SD-006 | SauceDemo | Products can be sorted by price, low to high | TC-SD-006 | `tests/saucedemo/test_login.py::test_products_can_be_sorted_by_price_low_to_high` | Confirm test name in source |
| REQ-SD-007 | SauceDemo | Checkout requires a first name | TC-SD-007 | `tests/saucedemo/test_checkout.py::test_checkout_requires_first_name` | Verify against current test suite |
| REQ-SD-008 | SauceDemo | A user can complete the checkout flow | TC-SD-008 | `tests/saucedemo/test_checkout.py::test_complete_checkout` | Verify against current test suite |
| REQ-SD-009 | SauceDemo | A product can be removed from the cart | TC-SD-009 | `tests/saucedemo/test_checkout.py::test_remove_product_from_cart` | Verify against current test suite |
| REQ-NX-001 | NEXUS | The dashboard loads successfully | TC-NX-001 | `tests/nexus/test_nexus.py::test_nexus_dashboard_loads` | Verify against current test suite |
| REQ-NX-002 | NEXUS | Main navigation pages can be accessed | TC-NX-002 | `tests/nexus/test_nexus.py::test_nexus_navigation_pages` | Verify against current test suite |
| REQ-NX-003 | NEXUS | The add-task form can be opened | TC-NX-003 | `tests/nexus/test_nexus.py::test_nexus_add_task_form_opens` | Verify against current test suite |
| REQ-NX-004 | NEXUS | A task can be added | TC-NX-004 | `tests/nexus/test_nexus_tasks.py::test_add_task` | Verify against current test suite |

## 3. Coverage Status Definitions

- **Covered and Passed:** The mapped test exists and passed in the latest recorded test run.
- **Covered and Failed:** The mapped test exists but failed in the latest recorded test run.
- **Not Verified:** The mapping or execution result has not yet been confirmed.
- **Not Automated:** The requirement is tested manually but has no corresponding automated test.

Do not mark a requirement as passed based on the existence of a test alone. Confirm the test name and execution result first.

## 4. Maintenance Guidelines

1. Assign a unique ID to every requirement and test case.
2. Update the matrix when requirements or test scripts change.
3. Verify test names against the actual source code.
4. Record results from real test executions.
5. Investigate requirements that have no corresponding test.
6. Keep this document synchronized with the manual test cases and automated test suite.

## 5. Limitations

This matrix is a starting point for the portfolio. The listed requirements are project-level testing objectives and should be checked against the actual application behavior and current test scripts. It does not establish complete requirements coverage by itself.
