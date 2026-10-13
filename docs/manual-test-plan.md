# Manual Test Cases — Selenium QA Automation Portfolio

## 1. Document Information

| Field | Details |
|---|---|
| Project | Selenium QA Automation Portfolio |
| Applications | SauceDemo and NEXUS |
| Test Type | Functional, negative, and UI testing |
| Test Environment | Windows 10, Microsoft Edge |
| Status | Initial test documentation |

## 2. SauceDemo Test Cases

**Test credentials:** `standard_user` / `secret_sauce`

| Test ID | Scenario | Steps | Expected Result |
|---|---|---|---|
| SD-LOGIN-001 | Valid login | Enter valid credentials and click Login | User reaches the inventory page |
| SD-LOGIN-002 | Invalid login | Enter an invalid username and password | An appropriate error message appears |
| SD-LOGIN-003 | Empty login | Leave both fields empty and click Login | Username-required validation appears |
| SD-LOGIN-004 | Locked-out account | Log in as `locked_out_user` | Access is denied with an error message |
| SD-INV-001 | Display products | Log in with valid credentials | Products are displayed |
| SD-CART-001 | Add product | Add Sauce Labs Backpack to the cart | Cart count updates to one |
| SD-CART-002 | Verify cart contents | Add the backpack and open the cart | The correct product appears |
| SD-SORT-001 | Sort by price ascending | Select price low to high | Prices appear in ascending order |
| SD-CHECK-001 | Complete checkout | Add a product, enter valid details, and finish checkout | Order confirmation appears |
| SD-CHECK-002 | Missing first name | Leave first name empty and continue | First-name validation appears |
| SD-CHECK-003 | Missing last name | Leave last name empty and continue | Last-name validation appears |
| SD-CHECK-004 | Missing postal code | Leave postal code empty and continue | Postal-code validation appears |

## 3. NEXUS Test Cases

| Test ID | Scenario | Steps | Expected Result |
|---|---|---|---|
| NX-DASH-001 | Dashboard loading | Open the NEXUS application | Dashboard loads successfully |
| NX-NAV-001 | Page navigation | Navigate between available pages | The selected pages open correctly |
| NX-TASK-001 | Open task form | Open the task creation form | The form is displayed |
| NX-TASK-002 | Add task | Enter task information and submit | The task is created and displayed |

## 4. Test Execution Record

Record actual results only after executing each manual test.

| Test ID | Actual Result | Status | Notes |
|---|---|---|---|
| SD-LOGIN-001 | To be recorded | Not Run | |
| SD-LOGIN-002 | To be recorded | Not Run | |
| SD-CART-001 | To be recorded | Not Run | |
| SD-CHECK-001 | To be recorded | Not Run | |
| NX-DASH-001 | To be recorded | Not Run | |
| NX-TASK-002 | To be recorded | Not Run | |

## 5. Execution Guidelines

1. Execute each scenario using the specified application and test data.
2. Compare the actual behavior with the expected result.
3. Record the execution status as Pass or Fail.
4. Record evidence and steps to reproduce whenever a test fails.
5. Report unexpected behavior using the project's bug-report template.

**Note:** The test cases above document intended checks. The manual execution statuses remain Not Run until each scenario has been manually executed and recorded.