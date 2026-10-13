# Test Plan — Selenium QA Automation Portfolio

## 1. Document Information

| Field | Details |
|---|---|
| Project | Selenium QA Automation Portfolio |
| Applications | SauceDemo and NEXUS |
| Prepared By | QA Portfolio Project |
| Test Approach | Manual and automated UI testing |
| Automation Framework | Selenium WebDriver with pytest |
| Local Browser | Microsoft Edge |
| CI Browser | Google Chrome |
| Document Status | Initial version |

## 2. Test Objectives

The objectives of this project are to:

- Verify important application functionality.
- Validate successful and unsuccessful login scenarios.
- Check product inventory, sorting, and shopping cart behavior.
- Validate checkout flows and required customer information.
- Verify selected NEXUS dashboard, navigation, and task-management behavior.
- Detect regressions through repeatable automated tests.
- Generate HTML test reports and capture screenshots when tests fail.

## 3. Scope of Testing

### In Scope

**SauceDemo**
- Login and authentication feedback.
- Product inventory display.
- Product sorting.
- Adding and removing products from the cart.
- Checkout completion.
- Required-field validation.

**NEXUS**
- Dashboard loading.
- Navigation between pages.
- Task form visibility.
- Task creation.

**Automation framework**
- Page Object Model organization.
- Explicit waits and pytest fixtures.
- Browser cleanup after tests.
- HTML test reporting.
- Failure screenshots.
- GitHub Actions execution.

### Out of Scope

- Production security or penetration testing.
- Load and performance testing.
- Formal API and database testing.
- Real payment processing.
- Testing application behavior that is not available in the current project environment.

## 4. Test Environment

| Component | Configuration |
|---|---|
| Programming Language | Python 3.11 |
| Automation Tool | Selenium WebDriver |
| Test Framework | pytest |
| Reporting | pytest-html |
| Local Operating System | Windows |
| Local Browser | Microsoft Edge |
| CI Environment | GitHub Actions on Ubuntu |
| CI Browser | Google Chrome |
| Source Control | Git and GitHub |

## 5. Test Approach

1. Review the application functionality and define test scenarios.
2. Prepare test data and preconditions.
3. Execute manual checks and automated tests.
4. Compare actual behavior against expected results.
5. Record failures and collect supporting evidence.
6. Generate reports and review test outcomes.
7. Re-run affected tests after changes.
8. Execute the full suite locally and through GitHub Actions.

## 6. Entry Criteria

- The application under test is accessible.
- Python and project dependencies are installed.
- The required browser is available.
- Test scripts and page objects are present.
- Valid test credentials are available where needed.

## 7. Exit Criteria

- All planned tests have an execution status.
- Failures have been investigated and documented.
- Critical test failures have been resolved or explicitly reported.
- The final test report is available.
- The tested code revision and results are recorded.

## 8. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Browser and driver incompatibility | Use Selenium Manager and verify CI browser setup |
| Slow page loading | Use explicit waits rather than relying on fixed delays |
| Unstable tests | Keep tests independent and verify preconditions |
| Environment differences | Run tests locally and through GitHub Actions |
| Unclear failures | Capture reports, screenshots, and error details |

## 9. Test Deliverables

- Automated test scripts.
- Reusable Page Object Model classes.
- Manual test case documentation.
- HTML test execution report.
- Failure screenshots when applicable.
- Sample defect report and requirements traceability matrix.
- GitHub Actions workflow results.

## 10. Current Baseline

During project development, the existing automated suite completed successfully with 17 passing tests locally and 17 passing tests in GitHub Actions.

These results describe the recorded baseline execution. They should not be interpreted as proof that every possible application behavior has been tested.

