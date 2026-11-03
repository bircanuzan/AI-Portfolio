# Privacy and accessibility gate with planned UAT

**Evidence status:** Test specification authored; no assertion of formal accessibility compliance, penetration test, backend security or deployment.

## Acceptance plan
| ID | Scenario | Expected |
|---|---|---|
| ESS01 | Valid fictional ID and simple topic | Creates in-memory case and readable confirmation |
| ESS02 | Missing fictional ID | Inline error, no case added |
| ESS03 | Payroll topic entered | Human Payroll/HR queue only, no payment authority |
| ESS04 | Employee relations entered | Safe human handoff with minimal detail |
| ESS05 | Enter actual-looking personal or bank/medical details | Warn user; instruct use of approved HR channel; never store sensitive detail |
| ESS06 | Page refreshed | No case data persisted |
| ESS07 | Screen reader form labels read | Field names and errors accessible |
| ESS08 | Keyboard-only submit | Interaction works with visible focus |
| ESS09 | Status of a newly generated case | 'Awaiting HR Review'; not fabricated processing progress |
| ESS10 | Employee requests a legally binding policy determination | Direct to qualified human owner |

## Data classification
Public demonstration: mock category names, generated ticket IDs and fictional case labels only. No user account, identity numbers, financial identifiers, salary, employment contract or medical records. Do not connect to a real employer without security assessment and explicit owner approval.

## Accessibility implementation targets
Use semantic native controls, explicit labels, text errors, sufficient contrast, logical tab order, keyboard activation and live-region feedback. A production accessibility claim requires independent testing across devices and assistive technology.

## Safety and human oversight
A browser mock-up must never be mistaken for an operational service. Every request is marked as a local demonstration and explicitly requires human review.
