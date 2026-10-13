# Bug Report — Selenium QA Automation Portfolio

## 1. Document Information

| Field | Details |
|---|---|
| Project | Selenium QA Automation Portfolio |
| Document Type | Software Defect Report |
| Status | Sample Template |
| Prepared By | QA Portfolio Project |

## 2. Bug Report Template

| Field | Description |
|---|---|
| Bug ID | Unique identifier, such as BUG-001 |
| Bug Title | Short description of the defect |
| Application | Application where the issue occurs |
| Environment | Operating system, browser, and application version |
| Severity | Impact of the defect on functionality |
| Priority | Urgency for fixing the defect |
| Preconditions | Required state before testing |
| Steps to Reproduce | Numbered steps to trigger the issue |
| Expected Result | Correct behavior according to requirements |
| Actual Result | Behavior observed during execution |
| Reproducibility | Whether the issue occurs consistently |
| Evidence | Screenshot, test report, logs, or other supporting details |
| Status | New, Open, In Progress, Fixed, Retest, or Closed |

## 3. Severity Definitions

| Severity | Meaning |
|---|---|
| Critical | A major failure that prevents essential system operation or causes severe impact |
| High | Important functionality is unavailable or seriously incorrect |
| Medium | Functionality is affected, but a workaround may exist |
| Low | Minor issue with limited functional impact or cosmetic impact |

## 4. Priority Definitions

| Priority | Meaning |
|---|---|
| P1 — Urgent | Requires immediate attention |
| P2 — High | Should be fixed as soon as possible |
| P3 — Normal | Can be addressed in the normal development cycle |
| P4 — Low | Can be scheduled for a later improvement |

Severity describes the impact of a defect. Priority describes how urgently the team should address it. The two values are related but are not necessarily the same.

## 5. Sample Defect — Demonstration Only

**Important:** The following is a hypothetical example to demonstrate defect-reporting skills. It is not a confirmed defect in SauceDemo or NEXUS.

| Field | Sample Details |
|---|---|
| Bug ID | DEMO-BUG-001 |
| Bug Title | Cart count does not update after adding a product |
| Application | SauceDemo |
| Environment | Windows, Microsoft Edge |
| Severity | Medium — hypothetical assessment |
| Priority | P2 — hypothetical assessment |
| Preconditions | User is logged in and the inventory page is displayed |
| Status | Example Only — Not Executed |

### Steps to Reproduce

1. Open SauceDemo.
2. Log in using valid test credentials.
3. Locate the Sauce Labs Backpack.
4. Click its Add to Cart button.
5. Observe the cart indicator.

### Expected Result

The cart indicator updates to show one item after the product is added.

### Hypothetical Actual Result

The cart indicator remains unchanged even though the Add to Cart button was clicked.

### Evidence

No screenshot or execution evidence is attached because this is a hypothetical example.

### Recommended Follow-Up

1. Execute the scenario in the target environment.
2. Record the actual result.
3. Capture a screenshot if the issue occurs.
4. Create a real defect record only if the unexpected behavior is observed.
5. Retest after a fix and update the defect status.

## 6. Defect Reporting Guidelines

- Report observable behavior rather than assumptions about the cause.
- Include clear, repeatable steps.
- Separate expected and actual results.
- Assign severity and priority based on impact and urgency.
- Attach relevant evidence when available.
- Never label a hypothetical defect as a verified finding.
